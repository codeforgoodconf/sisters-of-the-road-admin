# Sisters of the Road Cafe Admin and POS system

At Sisters of the Road Cafe, anyone can come in and purchase an affordable meal.
Those without the ability to afford a meal can trade volunteer time for cafe
credits. Currently, these volunteer credits are tracked manually, and the purpose
of this app is twofold:

- Provide a **Point of Sale** style interface, suitable for an iPad, for checking out with credits
- Provide an administrative view into volunteers' credit balances

With a system like this, the checkout process at the cafe can go more smoothly,
making running the checkout counter easier and faster. Administrators at the
cafe will be able to log into the Django Admin to look at volunteers, make
notes, and adjust balances as needed.

# Technology

This tool is a Django app. The POS interface will likely require some kind of
Javascript layer, but a heavy single page app is not required. Either standalone
vanilla JS, jQuery or Angular should suffice.

# License

GNU AGPL 3.0
