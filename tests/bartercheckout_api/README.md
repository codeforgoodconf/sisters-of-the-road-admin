# Backend API Tests

In this directory, you'll find the tests that are specifically geared towards testing the backend REST API.

### `client.py`

The default Django client for tests isn't sufficient for our needs. Instead, we use a client that is based on the Django Rest Framework `APIClient`.

### `base.py`

It is in this file that we define the fixtures that are specific to testing Django Rest Framework APIs. Most of the fixtures are straight forward. This:

```python
    @pytest.fixture
    def data(self):
        """Data to send to the server with the request."""
``` 

... allows you to simply define your own fixture called `data` that will be used during the test request. The interesting part of this APIViewTest is the common_subject, `get_response`. This means that every test method you define will implicitly call the get_response fixture (which will use the `kwargs` fixture). Moreover, the `response` fixture will be populated by your backend code as a result. That means that if you define a test like this:

```python
class TestWidgetAPIView(APIViewTest):
    def it_returns_a_widget(self, expected_widget, json):
        """This assumes we have created a fixture named `expected`"""
        assert json == expected_widget 
```

Just remember that by the time you get into your test function (_i.e._ in the body of `it_returns_a_widget` here), the request and the response has already happened and you merely need to evaluate if the results matched with what you expected to get.

There are also several convenience methods and a sub-class that helps with testing DRF ViewSets. Just remember, most everything in base.py is a pytest fixture. That means that you can simply pass the fixture name into a function that has been identified as being a test and the fixture will be available inside that function automatically. Some of these fixtures are like `json` above, they help you evaluate the results. Some of these fixtures (_e.g._ `Returns200`) are embedded with their own tests that will run automatically. And some of the fixtures are used to make sure your test state is set up like you want it to be. See `./bartercheckout_api/views/README.md` for examples.   