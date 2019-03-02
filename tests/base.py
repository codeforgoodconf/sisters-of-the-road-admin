from typing import Callable

import pytest


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
        raise NotImplementedError('Please override the `common_subject` fixture ' 'and provide a callable.')

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
