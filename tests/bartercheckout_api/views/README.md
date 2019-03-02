# Barter Checkout API Test Pattern

## What do you expect to get in return from the API?

First things first. Since you're going to get JSON as a response and since the testing methods will automatically convert that JSON to python for you, and since you know what the model fields are, you should first have a means of converting building up dictionaries to compare against the results. So here is a common method of expressing the expected return values:

```python
def express_barter_account(barter_account: BarterAccount) -> Dict[str, Any]:
    if barter_account:
        return {
            'id': barter_account.id,
            'customer_name': barter_account.customer_name,
            'balance': f'{barter_account.balance.amount:0.2f}',
            'last_add': str(barter_account.last_add),
            'last_subtract': str(barter_account.last_subtract),
        }

```

Given a barter account (note the python 3.6+ type hints help our IDE know what to expect), simply extract the barter account fields into a dictionary and return that dict. For a single barter account response, this is what we expect to get. What about if we are expecting to get many barter account results? That's where `pluralized()` comes into play:

```python
express_barter_accounts = pluralized(express_barter_account)
```

As outlined in `tests/util/README.md`, the pluralized method returns a function that takes an unpacked iterable and calls a function on each of the items and then returns a list of the results. In our case, we'll give it a bunch of barter accounts and it'll return a list of what we'd get back from `express_barter_account`.

##  What fixtures do you need to facilitate the tests?

For our tests, we first know that we need a bunch of barter_accounts in the database. So we can use the `lambda_fixture()` method along with the methods from pytest-factoryboy to not only create a bunch of realistic barter accounts in the database, but also to save a reference to them as a fixture that we can  use later.

```python
barter_accounts = lambda_fixture(lambda barter_account_factory: barter_account_factory.create_batch(5), autouse=True)
```

###### (Note: The `lambda_fixture()` and the `barter_account_factory` are detailed further in `tests/fixtures/README.md`.)

And although now we have 5 barter accounts in the database, it would still be more of a hassle than we'd like to index into that to pick out one special account to test against when we want to check the results for a specific account. So let's create another fixture:

```python
my_barter_account = lambda_fixture(lambda barter_account_factory: barter_account_factory.create(), autouse=True)
``` 

And with that, for this battery of tests, our database is all set up and ready to go.

###### (Note: by default, the data is inserted to a sqlite3 database that lives in memory. You won't see it on your disk and you don't have to worry about it corrupting any other databases.)

## The tests themselves

Now it's time to write the tests. First off, since we need access to the db, we have to use the `@pytest.mark.django_db` wrapper. Now, since this is testing a DjangoRestFramework ViewSet, we will subclass the main test class from `ViewSetTest`. Since `ViewSetTest` requires us to make a `list_url` and a `detail_url` fixture, we'll do that right off the bat.

```python
@pytest.mark.django_db
class TestBarterAccountApi(ViewSetTest):
    list_url = lambda_fixture(lambda: reverse('accounts-list'))
    detail_url = lambda_fixture(
        lambda my_barter_account: reverse('accounts-detail', kwargs={'pk': my_barter_account.id})
    )
```

Now that I've set up the overall test class information, I can start creating specific tests along with any specific contexts. So for example, we can test the listing of barter accounts:

```python
    class TestList(
        UsesGetMethod,
        UsesListEndpoint,

        Returns200,
    ):
        def it_lists_all_barter_accounts(self, my_barter_account, barter_accounts, json):
            expected = express_barter_accounts(
                *sorted([my_barter_account] + barter_accounts, key=lambda account: account.customer_name)
            )
            actual = json
            assert expected == actual
```

First note that the `UsesGetMethod` simply sets the `http_method` fixture to `get`. Since we're using a `ViewSetTest`, we must specify which endpoint, the list or the detail, this test will use (this is a list endpoint method). So those mixins are about the setup, whereas the `Returns200` is a mixin that implicitly runs a test to validate the returned response status value. Now notice how descriptive the actual test is. What do we expect? We expect it to list all the barter accounts that exist in the test database. There should be 6 of them. Since I set my `express_barter_accounts()` fixture, I can simply make an iterable out of all the available barter accounts (sorted on customer name because that is the default sort for this viewset). For debugging purposes, it's nice to explicitly store the json results into the value called actual, but this is not required. We finish with the assertion and this test is complete.

## Preconditions

There will be times when your API call will change the state of your database and so it would be good to be able to compare the condition of the database before the call and after the call. For this, we can use the `precondition_fixture()`:

```python
    class TestCreditAccount(
        UsesPostMethod,
    ):
        url = lambda_fixture(lambda detail_url: f'{detail_url}/credit')
        balance_before_call = precondition_fixture(lambda my_barter_account: my_barter_account.balance.amount)

        class ContextValidInput(
            Returns200,
        ):
            data = static_fixture({'amount': 2.25})

            def it_adds_credit_to_my_barter_account(self, my_barter_account, balance_before_call, json):
                assert json == {'balance': balance_before_call + Decimal(2.25)}
                actual = BarterAccount.objects.get(id=my_barter_account.id)
                assert actual.balance.amount == balance_before_call + Decimal(2.25)

```

First off, take note at the fact that we did not use the `UsesDetailEndpoint` fixture since this is an additional action endpoint. We have to take a step to build up the endpoint url which we do when we use the `url = ...` line. Take note of the `balance_before_call = ...` line, this is where we get our precondition value by using simple django commands on our model (which was defined earlier as a fixture). Now I created an inner class so I could separate out tests of valid input from tests of invalid input. The rest of the test follows from there. I set up the data fixture to pass along the required data for the call, in the function I validated the return value and I validated that the current status of the database was what I expected it to be.

The rest of the tests follow this general pattern. It's quite intuitive once you get the hang of it. 
 