import inspect
from copy import copy
from functools import partial
from typing import Any, Callable, List, TypeVar
from unittest.mock import Mock

import factory
import pytest_factoryboy
from factory.utils import OrderedBase
from pytest_factoryboy.fixture import (
    get_caller_module,
    get_factory_name,
    make_fixture,
)

__all__ = ['pluralized', 'register_factory']

T = TypeVar('T')
V = TypeVar('V')


def pluralized(fn: Callable[[T, Any], V]) -> Callable[..., List[V]]:
    """Return a method which maps a set of args onto fn()

        >>> fn = lambda d: d
        >>> fn({'id': 1})
        {'id': 1}
        >>> fn_pluralized = pluralized(fn)
        >>> fn_pluralized({'id': 1}, {'id': 2})
        [{'id': 1}, {'id': 2}]

    """

    def bulk_fn(*args: T, **kwargs) -> List[V]:
        mapped = map(lambda arg: fn(arg, **kwargs), args)
        return list(mapped)

    bulk_fn.__name__ = f'bulk_{fn.__name__}'

    return bulk_fn


def register_factory(factory_class=None, _module=None, **kwargs):
    """Register a factory, allowing kwargs to be passed to register()

    Usage:

        @register_factory(account=LazyFixture('account'))
        class VendorFactory(factory.DjangoModelFactory):
            class Meta:
                model = Vendor

        @register_factory
        class UserFactory(factory.DjangoModelFactory):
            class Meta:
                model = User

    """
    from . import MonkeyPatch

    if factory_class is None:
        _module = get_caller_module()
        return partial(register_factory, _module=_module, **kwargs)
    else:
        # XXX: haaaaaaaaaack.
        # The pytest-factoryboy plugin inspects the stack frame to determine
        # the module to place its "model_name" and "model_name_factory"
        # fixtures. Since we add a layer of indirection, we must determine the
        # module ourselves. Unfortunately, pytest-factoryboy doesn't let us
        # configure the module, so we patch get_caller_module to return the
        # correct module (and return it to normal afterward).
        if not _module:
            _module = get_caller_module()

        with MonkeyPatch() as mp:
            mp.setattr('pytest_factoryboy.fixture.get_caller_module',
                       Mock(return_value=_module))
            factory_class = pytest_factoryboy.register(factory_class, **kwargs)

        # We override the factory fixture, so it supports LazyFixtures
        factory_name = get_factory_name(factory_class)
        extra_fixtures = getattr(factory_class, '_pytest_fixtures', ())
        make_fixture(factory_name, _module,
                     _factory_class_lazy_fixture_evaluator,
                     args=extra_fixtures,
                     factory_class=factory_class)

        return factory_class


def wrap_factory_class(request, factory_class):
    decls = inspect.getmembers(factory_class)  # XXX: is this too broad?
    attrs = dict(vars(factory_class))
    for name, decl in decls:
        wrapped_decl = wrap_lazy_decl(request, name, decl)
        if wrapped_decl:
            attrs[name] = wrapped_decl

    # Expose pytest request to simplify LazyFixture resolution
    class Params:
        pytest_request = request

    attrs['Params'] = Params

    return type(factory_class.__name__, (factory_class,), attrs)


def copy_decl_ordering(old_decl, new_decl):
    """Curry the creation counter of old decl, so resolution order is preserved"""
    old_counter = getattr(old_decl, OrderedBase.CREATION_COUNTER_FIELD)
    setattr(new_decl, OrderedBase.CREATION_COUNTER_FIELD, old_counter)


def wrap_lazy_decl(request, name, decl):
    if isinstance(decl, (factory.RelatedFactory, factory.SubFactory)):
        # Ensure we pass the pytest request along to any sub factories
        decl = copy(decl)
        make_get_factory = lambda get_factory: lambda: _factory_class_lazy_fixture_evaluator(request, get_factory())
        decl.get_factory = make_get_factory(decl.get_factory)
        return decl


def _factory_class_lazy_fixture_evaluator(request, factory_class, *args, **kwargs):
    """
    This will be called when requesting the <model>_factory fixture. It turns
    LazyFixtures (which are unsupported by pytest-factoryboy inside the
    <model>_factory fixture) into LazyFunctions calling LazyFixture.evaluate
    with the pytest request.

    This allows the following:

        @register_factory
        class ModelFactory(factory.DjangoModelFactory):
            class Meta:
                model = Model

            account = LazyFixture('account')

    """
    factory_class = wrap_factory_class(request, factory_class)
    if hasattr(factory_class, '_pytest_initialize'):
        factory_class._pytest_initialize(request)

    return factory_class
