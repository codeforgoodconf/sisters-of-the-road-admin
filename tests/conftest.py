import pytest
from pytest_factoryboy import register

from tests.fixtures import BarterAccountFactory

register(BarterAccountFactory)


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
