from rest_framework.test import APIClient

from tests.util import flatten_decl


class DeclarativeAPIClient(APIClient):
    """DRF test client which processes tests.api.decl stuff passed as data"""

    def _encode_data(self, data, format=None, content_type=None):
        if data:
            data = flatten_decl(data)

        return super()._encode_data(data, format, content_type)
