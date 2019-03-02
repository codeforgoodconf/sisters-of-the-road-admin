import wrapt

__all__ = ['ReadOnly', 'Any', 'Optional', 'flatten_decl']


class ReadOnly(wrapt.ObjectProxy):
    """Mark a value as read-only (shouldn't be sent to server)

    Any value marked as ReadOnly will be stripped by the API test client when
    POSTed, PUT, or PATCHed. This allows the developer to declare data in one
    place, without needing separate sources of authority for data sent to the
    server and data coming back from the server.

    Examples of functionality:

    >>> obj = ReadOnly('test string')
    >>> obj
    'test string'
    >>> obj + ' theory'
    'test string theory'

    >>> from tests.util import flatten_decl
    >>> data = {'name': 'Justin', 'active': ReadOnly(True)}
    >>> data == {'name': 'Justin'}
    False
    >>> data == {'name': 'Justin', 'active': True}
    True
    >>> flatten_decl(data)
    {'name': 'Justin'}

    Use case:

        def test_my_stuff(client):
            data = {
                'name': 'Justin',
                'active': ReadOnly(True),
            }

            # Only `{'name': 'Justin'}` will reach the server
            # (The API test client calls `flatten_dict` for us)
            response = client.post('/users', data=data)

            expected = data
            actual = response.json()

            # This will test expected['active'] == True
            assert actual == expected
    """

    _is_read_only = True

    @classmethod
    def is_read_only(cls, obj):
        return getattr(obj, '_is_read_only', False)


class Any:
    """Meta-value which compares True to any object (of the specified type(s))

    Examples of functionality:

    >>> Any() == 'stuff'
    True
    >>> Any() == 1
    True
    >>> Any() == None
    True
    >>> Any() == object()
    True

    >>> Any(int) == 1
    True
    >>> Any(int) == '1'
    False
    """

    def __init__(self, *allowed_types):
        self.allowed_types = allowed_types

    def __eq__(self, other):
        if self.allowed_types:
            return isinstance(other, self.allowed_types)
        else:
            return True


class Optional:
    """Meta-value which compares True to None or the optionally specified value

    Examples of functionality:

    >>> Optional() == None
    True
    >>> Optional() is None  # this will not work!
    False
    >>> Optional(24) == 24
    True
    >>> Optional(24) == None
    True

    >>> Optional(Any(int)) == 1
    True
    >>> Optional(Any(int)) == None
    True
    >>> Optional(Any(int)) == '1'
    False
    """

    def __init__(self, value=None):
        self.value = value

    def __eq__(self, other):
        return other in (None, self.value)


def flatten_decl(v):
    """Process declarative items and return a payload to be sent to server"""
    if isinstance(v, (tuple, list)):
        v = _flatten_decl_list(v)
    elif isinstance(v, dict):
        v = _flatten_decl_dict(v)
    return v


def _flatten_decl_dict(d):
    return {key: flatten_decl(value) for key, value in d.items() if not ReadOnly.is_read_only(value)}


def _flatten_decl_list(l):
    iterable_type = type(l)
    return iterable_type(flatten_decl(value) for value in l if not ReadOnly.is_read_only(value))
