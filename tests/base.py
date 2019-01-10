from typing import Callable, Type

import pytest
from rest_framework import status

from tests.fixtures.utils import lambda_fixture


class CommonSubjectTestMixin:
    """Abstract mixin for test contexts revolving around a common target

    Imperative tests are intensive to read. To grok what a test is *actually*
    trying to prove requires inspecting many lines of code which are ultimately
    inessential boilerplate.

    If, instead, we group our tests by the Subject being prodded, we can cordon
    off boilerplate to a single location, leaving only the juicy bits left to
    read.

    This mixin will call a single function for every test method, and provide
    its return value as a fixture, which is always evaluated after all other
    fixtures (so they can still be used for setup). The args passed in this
    function call can be customized by overriding the args/kwargs fixtures.

    Test contexts defined underneath this mixin are free to override
    args/kwargs, and create/override fixtures to setup the environment for the
    function call. This encourages named, well-defined contexts for testing
    the common subject from different viewpoints.

    This pattern also encourages slimmer tests, ideally responsible for testing
    a single aspect of the common subject and named descriptively. The upshot
    of this is all issues can be reported in one test run – as opposed to
    monolith tests, where fixing an issue and re-running the test suite reveals
    the next thing to fix.
    """

    @pytest.fixture
    def common_subject(self, *args) -> Callable:
        """The method being tested in this context"""
        raise NotImplementedError('Please override the `common_subject` fixture '
                                  'and provide a callable.')

    @pytest.mark.late  # this ensures the fixture is executed at end of setup
    @pytest.fixture(autouse=True)
    def rval(self, get_subject_rval, all_preconditions):
        """The return value from invoking the common subject in this env

        To perform any post-processing on the return value (like parsing the
        JSON of an HTTP response), it's recommended to define another fixture
        that requests `rval`.
        """
        return get_subject_rval()

    @pytest.fixture
    def get_subject_rval(self, common_subject, args, kwargs):
        """A 0-arg method which invokes common_subject and returns its result

        Override this to customize how the common subject is invoked.
        """

        def get_subject_rval():
            return common_subject(*args, **kwargs)

        return get_subject_rval

    @pytest.fixture
    def args(self) -> tuple:
        """Inline arguments to be passed when invoking common_subject"""
        return ()

    @pytest.fixture
    def kwargs(self) -> dict:
        """Keyword arguments to be passed when invoking common_subject"""
        return {}

    @pytest.fixture
    def all_preconditions(self, preconditions, marked_preconditions):
        """Metafixture to request preconditions declared by any means

        Preconditions can be declared by overriding the `preconditions`
        fixture, using the @pytest.mark.precondition('fixture_name') marker,
        or by using the `precondition_fixture()` lambda fixture declaration.
        `all_preconditions` loads each of these types of preconditions.

        `rval` requests `all_preconditions`, instead of directly requesting
        `preconditions` and `marked_preconditions`, so the user may customize
        precondition loading without having to completely redefine `rval`.
        """

    @pytest.fixture
    def preconditions(self):
        """Any preconditions to be evaluated before the subject is invoked

        This fixture is requested by the rval fixture, before calling
        get_subject_rval(). By overriding this fixture, one can request other
        fixtures to be evaluated as "preconditions".

        Example:

            class TestMyStuff(CommonSubjectTestMixin):
                common_subject = lambda_fixture(lambda: MyModel.objects.all().delete())

                initial_count = lambda_fixture(lambda: MyModel.objects.count())
                preconditions = lambda_fixture('initial_count')

                def it_deletes_things(self, initial_count):
                    assert initial_count == 1
                    assert MyModel.objects.count() == 0

        """

    @pytest.fixture
    def marked_preconditions(self, request):
        """Load any fixtures declared with @pytest.mark.precondition('name')

        NOTE: this is how precondition_fixture() declares preconditions
        """
        precondition_marks = tuple(request.node.iter_markers('precondition'))
        precondition_fixtures = [mark.args[0] for mark in precondition_marks]

        for fixturename in precondition_fixtures:
            request.getfixturevalue(fixturename)


class APIViewTest(CommonSubjectTestMixin):
    """Base class providing default fixtures for DRF API views

    Be sure to subclass this in any viewset tests using the APITest harness.
    By requiring this instead of defining fixtures inside APITest,
    parametrization can be used to override fixtures, avoiding large subclasses
    """

    # @pytest.fixture
    # def client(self, unauthed_client):
    #     """API client to perform requests with
    #
    #     If you require a particular user to be authenticated, set this fixture
    #     to a different client (e.g. "admin_client"):
    #
    #         @pytest.fixture
    #         def client(admin_client):
    #             return admin_client
    #
    #         # This can also be expressed more compactly with lambda_fixture
    #         client = lambda_fixture('admin_client')
    #
    #     Or, perform authentication yourself:
    #
    #         @pytest.fixture
    #         def client(unauthed_client, my_user):
    #             unauthed_client.force_authenticate(user=my_user)
    #             return unauthed_client
    #
    #     """
    #     return unauthed_client

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

# class UsesGetMethod:
#     http_method = static_fixture('get')
#
#
# class UsesPostMethod:
#     http_method = static_fixture('post')
#
#
# class UsesPutMethod:
#     http_method = static_fixture('put')
#
#
# class UsesPatchMethod:
#     http_method = static_fixture('patch')
#
#
# class UsesDeleteMethod:
#     http_method = static_fixture('delete')
#

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
