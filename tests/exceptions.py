__all__ = ['DisabledFixtureError', 'NotImplementedFixtureError']


class DisabledFixtureError(Exception):
    """Thrown when a disabled fixture has been requested by a test or fixture

    See tests.util.fixtures.disabled_fixture
    """
    pass


class NotImplementedFixtureError(NotImplementedError):
    """Thrown when an abstract fixture has been requested

    See tests.util.fixtures.not_implemented_fixture
    """
    pass
