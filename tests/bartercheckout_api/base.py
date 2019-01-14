from typing import Type

import pytest
from rest_framework import status

from tests.bartercheckout_api.client import DeclarativeAPIClient
from tests.base import CommonSubjectTestMixin
from tests.fixtures.utils import lambda_fixture, static_fixture


class APIViewTest(CommonSubjectTestMixin):
    """Base class providing default fixtures for DRF API views

    Be sure to subclass this in any viewset tests using the APITest harness.
    By requiring this instead of defining fixtures inside APITest,
    parametrization can be used to override fixtures, avoiding large subclasses
    """

    @pytest.fixture
    def client(self):
        """Use a custom client based on the Django Rest Framework test
        client, APIClient, instead of the Django test client.
        """
        return DeclarativeAPIClient()

    @pytest.fixture
    def http_method(self):
        """Name of API client method to perform request with"""
        return 'get'

    @pytest.fixture
    def url(self):
        """URL to be requested

        Use reverse() to generate URLs:

            @pytest.fixture
            def url():
                return reverse('viewset_basename-list')

            # This can also be expressed more compactly with lambda_fixture
            url = lambda_fixture(lambda: reverse('viewset_basename-list'))

            # Other fixtures can be requested to use in URL generation:
            url = lambda_fixture(lambda vendor: reverse('vendors-detail',
                                                        args=(vendor.pk,)))

        """
        raise NotImplementedError('Please define a url fixture')

    @pytest.fixture
    def headers(self):
        """Headers to pass along with the request"""
        return {}

    @pytest.fixture
    def data(self):
        """Data to send to the server with the request."""

    @pytest.fixture
    def get_response(self, http_method, client):
        """API client test method called to perform actual request"""
        return getattr(client, http_method)

    @pytest.fixture
    def response(self, rval):
        """Response from server; the result of calling the API client method"""
        return rval

    @pytest.fixture
    def json(self, response):
        """The JSON body of the API response"""
        return response.json()

    @pytest.fixture
    def results(self, json):
        """The value of the 'results' key in the API response JSON body"""
        return json['results']

    # Configuration for CommonSubjectTestMixin below

    @pytest.fixture
    def common_subject(self, get_response):
        return get_response

    @pytest.fixture
    def args(self, url):
        return (url,)

    @pytest.fixture
    def kwargs(self, data, headers):
        return dict(data=data, headers=headers)


class ViewSetTest(APIViewTest):
    """DRF view test w/ ViewSet-specific conveniences"""

    @pytest.fixture
    def list_url(self):
        """Return the list URL for the viewset. See UseListEndpoint"""
        raise NotImplementedError('Please define a list_url fixture')

    @pytest.fixture
    def detail_url(self):
        """Return the detail URL for the viewset. See UseDetailEndpoint"""
        raise NotImplementedError('Please define a detail_url fixture')


######################
# URL / PATH / ROUTE #
######################
#
# Declare which ViewSet URL route to request

class UsesListEndpoint:
    url = lambda_fixture('list_url')


class UsesDetailEndpoint:
    url = lambda_fixture('detail_url')


###############
# HTTP METHOD #
###############
#
# Declare which HTTP method used when performing the request

class UsesGetMethod:
    http_method = static_fixture('get')


class UsesPostMethod:
    http_method = static_fixture('post')


class UsesPutMethod:
    http_method = static_fixture('put')


class UsesPatchMethod:
    http_method = static_fixture('patch')


class UsesDeleteMethod:
    http_method = static_fixture('delete')


########################
# ENFORCE STATUS CODES #
########################
#
# Declare which HTTP status code is returned from the endpoint

class _ReturnsSpecificStatusMeta(type):
    # This metaclass allows ReturnStatus(xyz) to return a subclass of
    # ReturnStatus with the expected_status_code fixture defined as xyz.

    def __call__(cls, *args, **kwargs) -> Type['ReturnsStatus']:
        if cls is not ReturnsStatus:
            return super().__call__(*args, **kwargs)

        status_code, = args

        class ReturnsXYZ(ReturnsStatus):
            @pytest.fixture
            def expected_status_code(self):
                return status_code

        ReturnsXYZ.__name__ = f'Returns{status_code}'
        return ReturnsXYZ


class ReturnsStatus(metaclass=_ReturnsSpecificStatusMeta):
    """Includes test which checks response for the HTTP specified status code
    """

    @pytest.fixture
    def expected_status_code(self):
        raise NotImplementedError(
            'Please define the expected_status_code fixture. Alternatively, '
            'subclass ReturnStatus(code) instead of the bare ReturnStatus.')

    def it_should_return_expected_status_code(self, response, expected_status_code):
        assert response.status_code == expected_status_code

    # this appeases code sense, which may not be able to understand how the
    # metaclass allows using instantiation syntax without really instantiating.
    def __init__(self, status_code: int): pass

    del __init__


Returns200 = ReturnsStatus(status.HTTP_200_OK)
Returns201 = ReturnsStatus(status.HTTP_201_CREATED)
Returns204 = ReturnsStatus(status.HTTP_204_NO_CONTENT)

Returns400 = ReturnsStatus(status.HTTP_400_BAD_REQUEST)
Returns401 = ReturnsStatus(status.HTTP_401_UNAUTHORIZED)
Returns403 = ReturnsStatus(status.HTTP_403_FORBIDDEN)
Returns404 = ReturnsStatus(status.HTTP_404_NOT_FOUND)
Returns405 = ReturnsStatus(status.HTTP_405_METHOD_NOT_ALLOWED)
