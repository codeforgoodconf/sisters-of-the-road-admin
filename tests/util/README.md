# Tests Util

The utility methods located here are to facilitate some of the neat stuff that makes the declarative testing work. There won't be much need to worry about this stuff.

## Pluralized

One function that will be of interest, possibly, is the `pluralized()` function. This method takes a function and then when called with an iterable of inputs, calls that function on each of those inputs. This is very handy for creating a list of expected value dictionaries.
