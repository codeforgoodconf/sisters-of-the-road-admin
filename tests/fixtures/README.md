# Testing Fixtures

In pytest, a fixture is a globally available function that is used for dependency injection. The special feature of fixtures is that any function that has been identified by pytest as being a test function has access to one of these fixtures just by passing the fixture name as a parameter to the function. This directory has our fixtures and utilities relating to fixtures.

# Lambda Fixtures

You can always define a fixture like this:

```python
@pytest.fixture
def detail_url(my_barter_account):
    return reverse('accounts-detail', kwargs={'account_id': my_barter_account.id})
```

But it is often more succinct to do this:

```python
detail_url = lambda_fixture(lambda my_barter_account: reverse('accounts-detail', kwargs-{my_barter_account.id}))
```

The lambda fixture code will automatically create and register fixtures for you. What's more there are static fixtures so that you can easily create fixtures out of code that isn't dynamic. _e.g._

```python
data = static_fixture({'amount': 2.50})
``` 

And there is a precondition fixture which allows you to store what _was_ true about your state before you made the api call so you can compare the resulting state against it.