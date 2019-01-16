import functools
import inspect
import wrapt
from types import ModuleType
from typing import Any, Callable, Iterable, Union

import pytest

from tests.exceptions import DisabledFixtureError, NotImplementedFixtureError

__all__ = ['lambda_fixture', 'static_fixture', 'error_fixture',
           'disabled_fixture', 'not_implemented_fixture',
           'precondition_fixture', 'LambdaFixture']


def lambda_fixture(fixture_name_or_lambda: Union[str, Callable] = None,
                   *other_fixture_names: Iterable[str],
                   bind=False,
                   scope="function", params=None, autouse=False, ids=None, name=None):
    """Use a fixture name or lambda function to compactly declare a fixture

    Usage:

        class DescribeMyTests:
            url = lambda_fixture('list_url')
            updated_name = lambda_fixture(lambda vendor: vendor.name + ' updated')


    :param fixture_name_or_lambda: Either the name of another fixture, or a
        lambda function, which can request other fixtures with its params. If
        None, this defaults to the name of the attribute containing the lambda_fixture.

    :param bind: Set this to true to pass self to your fixture. It must be the
        first parameter in your fixture. This cannot be true if using a fixture
        name.

    """
    if other_fixture_names:
        fixture_names_or_lambda = (fixture_name_or_lambda,) + other_fixture_names
    else:
        fixture_names_or_lambda = fixture_name_or_lambda

    return LambdaFixture(fixture_names_or_lambda, bind=bind, scope=scope,
                         params=params, autouse=autouse, ids=ids, name=name)


def static_fixture(value: Any, **kwargs):
    """Compact method for defining a fixture that returns a static value
    """
    return lambda_fixture(lambda: value, **kwargs)


RAISE_EXCEPTION_FIXTURE_FUNCTION_FORMAT = '''
def raise_exception({args}):
    raise error_fn({kwargs})
'''


def error_fixture(error_fn: Callable, **kwargs):
    """Fixture whose usage results in the raising of an exception

    Usage:

        class DescribeMyTests:
            url = error_fixture(lambda request: Exception(
                f'Please override the {request.fixturename} fixture!'))

    :param error_fn: fixture method which returns an exception to raise. It may
        request pytest fixtures in its arguments

    """
    proto = tuple(inspect.signature(error_fn).parameters)
    args = ', '.join(proto)
    kwargs = ', '.join(f'{arg}={arg}' for arg in proto)

    source = RAISE_EXCEPTION_FIXTURE_FUNCTION_FORMAT.format(
        args=args,
        kwargs=kwargs,
    )

    ctx = {'error_fn': error_fn}
    exec(source, ctx)

    raise_exception = ctx['raise_exception']
    return lambda_fixture(raise_exception)


def disabled_fixture():
    """Mark a fixture as disabled – using the fixture will raise an error

    This is useful when you know any usage of a fixture would be in error. When
    using disabled_fixture, pytest will raise an error if the fixture is
    requested, so errors can be detected early, and faulty assumptions may be
    avoided.

    Usage:

        class DescribeMyListOnlyViewSet(ViewSetTest):
            list_route = lambda_fixture(lambda: reverse('...'))
            detail_route = disabled_fixture()

            class DescribeRetrieve(UsesDetailRoute):
                def test_that_should_throw_error():
                    print('I should never be executed!')

    """

    def build_disabled_fixture_error(request):
        msg = (f'Usage of the {request.fixturename} fixture has been disabled '
               f'in the current context.')
        return DisabledFixtureError(msg)

    return error_fixture(build_disabled_fixture_error)


def not_implemented_fixture():
    """Mark a fixture as abastract – requiring definition/override by the user

    This is useful when defining abstract base classes requiring implementation
    to be used correctly.

    Usage:

        class MyBaseTest:
            list_route = not_implemented_fixture()

        class TestThings(MyBaseTest):
            list_route = lambda_fixture(lambda: reverse(...))

    """

    def build_not_implemented_fixture_error(request):
        msg = (f'Please define/override the {request.fixturename} fixture in '
               f'the current context.')
        return NotImplementedFixtureError(msg)

    return error_fixture(build_not_implemented_fixture_error)


def precondition_fixture(*args, **kwargs):
    """Fixture to be evaluated before the Common Subject is invoked

    NOTE: this fixture only makes sense when using CommonSubjectTestMixin, or
          its subclasses (e.g. ViewSetTest).

    Usage:

        class TestMyStuff(CommonSubjectTestMixin):
            common_subject = static_fixture(datetime.utcnow)
            before = precondition_fixture(lambda: datetime.utcnow())

            def it_evaluates_precondition_before_subject(self, rval, before):
                assert before < rval

    """
    return PreconditionFixture(*args, **kwargs)


class LambdaFixture(wrapt.ObjectProxy):
    # NOTE: pytest won't apply marks unless the markee has a __call__ and a
    #       __name__ defined.
    __name__ = '<lambda-fixture>'

    bind: bool
    fixture_kwargs: dict
    fixture_func: Callable
    has_fixture_func: bool
    parent: Union[type, ModuleType]

    def __init__(self, fixture_names_or_lambda, bind=False, **fixture_kwargs):
        self.bind = bind
        self.fixture_kwargs = fixture_kwargs
        self.fixture_func = self._not_implemented
        self.has_fixture_func = False
        self.parent = None

        #: pytest fixture info definition
        self._pytestfixturefunction = pytest.fixture(**fixture_kwargs)

        if fixture_names_or_lambda is not None:
            self.set_fixture_func(fixture_names_or_lambda)

        elif fixture_kwargs.get('params'):
            # Shortcut to allow `lambda_fixture(params=[1,2,3])`
            self.set_fixture_func(lambda request: request.param)

    def __call__(self, *args, **kwargs):
        if self.bind:
            args = (self.parent,) + args
        return self.fixture_func(*args, **kwargs)

    def _not_implemented(self):
        raise NotImplementedError(
            'The fixture_func for this LambdaFixture has not been defined. '
            'This is a catastrophic error!')

    def set_fixture_func(self, fixture_names_or_lambda):
        self.fixture_func = self.build_fixture_func(fixture_names_or_lambda)
        self.has_fixture_func = True

        # NOTE: this initializes the ObjectProxy
        super().__init__(self.fixture_func)

    def build_fixture_func(self, fixture_names_or_lambda):
        if callable(fixture_names_or_lambda):
            real_fixture_func = fixture_names_or_lambda

            # We create a new method with the same signature as the passed
            # method, which simply calls the passed method – this is so we can
            # modify __name__ and other properties of the function without fear
            # of overwriting functions unrelated to the fixture. (A lambda need
            # not be used – a method imported from another module can be used.)

            @functools.wraps(real_fixture_func)
            def insulator(*args, **kwargs):
                return real_fixture_func(*args, **kwargs)

            return insulator

        else:
            if self.bind:
                raise ValueError(
                    'bind must be False if requesting a fixture by name')

            fixture_names = fixture_names_or_lambda
            if isinstance(fixture_names, str):
                fixture_names = (fixture_names,)

            # Create a new method with the requested parameter, so pytest can
            # determine its dependencies at parse time. If we instead use
            # request.getfixturevalue, pytest won't know to include the fixture
            # in its dependency graph, and will vomit with "The requested
            # fixture has no parameter defined for the current test."
            name = 'fixture__' + '__'.join(fixture_names)  # XXX: will this conflict in certain circumstances?
            return create_identity_lambda(name, *fixture_names)

    def contribute_to_parent(self, parent: Union[type, ModuleType], name: str, **kwargs):
        """Setup the LambdaFixture for the given class/module
        This method is called during collection, when a LambdaFixture is
        encountered in a module or class. This method is responsible for saving
        any names and setting any attributes on parent as necessary.
        """
        is_in_class = isinstance(parent, type)
        is_in_module = isinstance(parent, ModuleType)
        assert is_in_class or is_in_module

        if is_in_module and self.bind:
            raise ValueError(f'bind=True cannot be used at the module level. '
                             f'Please remove this arg in the {name} fixture in {parent.__file__}')

        if not self.has_fixture_func:
            # If no fixture definition was passed to lambda_fixture, it's our
            # responsibility to define it as the name of the attribute. This is
            # handy if ya just wanna force a fixture to be used, e.g.:
            #    do_the_thing = lambda_fixture(autouse=True)
            self.set_fixture_func(name)

        self.__name__ = name
        self.__module__ = parent.__module__ if is_in_class else parent.__name__
        self.parent = parent

    # These properties are required in order to expose attributes stored on the
    # LambdaFixture proxying instance without prefixing them with _self_

    @property
    def bind(self):
        return self._self_bind

    @bind.setter
    def bind(self, value):
        self._self_bind = value

    @property
    def fixture_kwargs(self):
        return self._self_fixture_kwargs

    @fixture_kwargs.setter
    def fixture_kwargs(self, value):
        self._self_fixture_kwargs = value

    @property
    def fixture_func(self):
        return self._self_fixture_func

    @fixture_func.setter
    def fixture_func(self, value):
        self._self_fixture_func = value

    @property
    def has_fixture_func(self):
        return self._self_has_fixture_func

    @has_fixture_func.setter
    def has_fixture_func(self, value):
        self._self_has_fixture_func = value

    @property
    def parent(self):
        return self._self_parent

    @parent.setter
    def parent(self, value):
        self._self_parent = value

    @property
    def _pytestfixturefunction(self):
        return self._self__pytestfixturefunction

    @_pytestfixturefunction.setter
    def _pytestfixturefunction(self, value):
        self._self__pytestfixturefunction = value


class PreconditionFixture(LambdaFixture):
    def contribute_to_parent(self, parent: Union[type, ModuleType], name: str, **kwargs):
        # Add precondition marker to class. CommonSubjectTestMixin.marked_preconditions
        # will load all fixtures named by this marker.
        pytest.mark.precondition(name)(parent)

        return super().contribute_to_parent(parent, name, **kwargs)


_IDENTITY_LAMBDA_FORMAT = '''
{name} = lambda {argnames}: ({argnames})
'''


def create_identity_lambda(name, *argnames):
    source = _IDENTITY_LAMBDA_FORMAT.format(name=name, argnames=', '.join(argnames))
    context = {}
    exec(source, context)

    fixture_func = context[name]
    return fixture_func
