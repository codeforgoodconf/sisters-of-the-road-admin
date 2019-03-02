# Backend Testing

Testing is hard. Testing Django can be even harder because of the amount of boilerplate required to get your tests off the ground. The purpose of all the scary-looking code (at first) in here is to make it easy for you to do the actual business of writing tests. This will be an initial overview of what you'll find in this test framework and there will be other READMEs as required in the sub-directories.

## APIViewTest Class

In `base.py` you'll find a class full of fixtures that tests of the API views all have in common. 