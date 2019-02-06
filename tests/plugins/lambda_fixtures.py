"""
This pytest plugin inspects all test modules and classes found during
collection and converts lambda_fixture definitions into actual pytest fixtures.
This cannot be done when `lambda_fixture` is called, because the name of the
attribute is not known then. Only after the module or class is defined can we
learn the name.
"""
import inspect
from typing import List, Tuple

import pytest
from _pytest.python import Module


@pytest.hookimpl(hookwrapper=True)
def pytest_pycollect_makemodule(path, parent):
    outcome = yield
    module: Module = outcome.get_result()  # will raise if outcome was exception

    process_lambda_fixtures(module.module)


def pytest_pycollect_makeitem(collector, name, obj):
    if inspect.isclass(obj):
        process_lambda_fixtures(obj)


def process_lambda_fixtures(parent):
    """Turn all lambda_fixtures in a class/module into actual pytest fixtures
    """
    # Local import, so we don't unintentionally import tests.util.assertions,
    # preventing pytest from rewriting its bytecode for assertion introspection
    from tests.fixtures.utils import LambdaFixture

    lfix_attrs: List[Tuple[str, LambdaFixture]] = (
        inspect.getmembers(parent, lambda o: isinstance(o, LambdaFixture))
    )

    for name, attr in lfix_attrs:
        attr.contribute_to_parent(parent, name)

    return parent
