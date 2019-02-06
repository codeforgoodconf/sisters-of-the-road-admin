import pytest
from pytest_factoryboy import register

from tests.fixtures import BarterAccountFactory

register(BarterAccountFactory)

pytest_plugins = (
    # Place any modules here which contain assert statements for testing.
    # (pytest will only perform its bytecode-rewriting magic on test modules
    #  and plugins. asserts performed elsewhere won't get the benefit of
    #  introspection in pytest's output)
    'tests.bartercheckout_api.base',

    # Load in our fixtures
    'tests.plugins.lambda_fixtures',
)


@pytest.fixture(scope='session')
def django_db_setup(request):
    """pytest-django passes pytest's verbosity along to Django when it
    creates the test databases. Passing -vv to pytest means Django's
    commands get verbosity=2, which prints a lot of useless information.
    But only passing -v, or not at all means pytest doesn't print out
    full error messages (like diffs on failed assertions).

    So, this fixture lowers pytest's verbosity while pytest-django sets
    up the databases.
    """

    original_verbosity = request.config.option.verbose

    request.config.option.verbose = 0
    try:
        rval = request.getfixturevalue('django_db_setup')
    finally:
        request.config.option.verbose = original_verbosity

    yield rval


def _patch_lazy_fixture():
    """
    pytest-factoryboy's LazyFixture does not inherit from factory's
    BaseDeclaration, and thus does not record its order relative to other
    declarations. To avoid unexpected behaviour in resolution (e.g. a
    LazyFixture being resolved after other declarations, despite being declared
    before them), we inject BaseDeclaration into LazyFixture's base classes.

    We also augment LazyFixture evaluation to support usage from both model
    attribute fixtures (e.g. `team__name`) and manual factory class
    instantiation.
    """
    import pytest_factoryboy
    from factory.declarations import BaseDeclaration

    class OrderedLazyFixture(pytest_factoryboy.LazyFixture, BaseDeclaration):
        real_evaluate = pytest_factoryboy.LazyFixture.evaluate

        def evaluate(self, instance, step=None, extra=None):
            """
            We overload this method, so it can be called by pytest_factoryboy's
            model fixtures (e.g. `team` of `TeamFactory`) as well as in factory
            class fixtures (e.g. `team_factory`).

            The model fixtures grab their declarations' values from individual
            fixtures (e.g. `team__name`). To support LazyFixtures in these decl
            fixtures, pytest_factoryboy evaluates them itself.

            pytest_factoryboy does not support using LazyFixtures with factory
            class fixtures out of the box. We support this ourselves by
            injecting `pytest_request` as a Parameter, which we can reference
            as a dependency when the factory class evaluates our LazyFixture
            by passing a Resolver as instance (as well as step and extra).
            """

            if step is None and extra is None:
                request = instance
            else:
                # pytest_request is added as a Parameter
                # by our _factory_class_lazy_fixture_evaluator
                request = instance.pytest_request
            return self.real_evaluate(request)

    pytest_factoryboy._LazyFixture = pytest_factoryboy.LazyFixture
    pytest_factoryboy.LazyFixture = OrderedLazyFixture


def _disable_pytest_django_fixtures():
    """
    pytest-django offers some convenient fixtures, such as `client` and
    `admin_user`. Unfortunately, this can cause lots of confusion, when you
    expect `client` to refer to the fixture defined in this module but instead
    get pytest-django's.

    To mitigate this, we disable conflicting fixtures by deleting them before
    they're collected by pytest.
    """
    import pytest_django.plugin

    for name in 'client', 'admin_user', 'admin_client':
        delattr(pytest_django.plugin, name)


_patch_lazy_fixture()
_disable_pytest_django_fixtures()
