import pytest
from faker import Faker

__all__ = ['faker']


@pytest.fixture
def faker():
    """Convenience fixture to access Faker providers

    Usage:

        def test_my_stuff(faker):
            title = f"{faker.name()}'s Thing"
    """
    return Faker()
