Customers at Sisters of the Road Cafe can get a meal for just $1.25. The cafe also serves coffee and sides. Customers can pay with cash, SNAP/EBT, or volunteer (barter) credit. To understand the mission values of the orgnaization and to understand the needs of the cafe, its helpful to spend some time reading the about the Cafe here: https://sistersoftheroad.org

The remainder of this document described the functionality this project can bring to the cafe through a web application designed for them. There are two parts of the application, the UI used by counter staff on an iPad, and the Django admin used by admin staff on a desktop computer. 


## Barter accounts - this is mostly implemented

A customer can trade an hour of work in the cafe for $6 to spend on meals and coffee. The first time a customer volunteers, an admin will need to create an account for them. 

Once their account is added, their balance can be added to or spent from by the counter staff. Counter staff will search for the account on the main page of the app. Account names are flexible. We do not assume a first name or last name. 

Once the counter staff find the account of the customer and taps on it, they can add credit to the account, or they can spend money from the account to buy a meal or a card. Barter cards are an alternate way of using barter credits. Some customers primarily use cards, but a customer that uses an account may want to buy a card to share with another customer, or because their account has reached the maximum limit of $50.

All prices at the cafe are in increments of $0.25, so it is only possible to spend money in $0.25 increments in the barter app. Accounts cannot go above $50 or below $0. 

Once the counter staff has entered the transaction information, the customer will be able to confirm the transaction on the iPad, possibly by entering their initials or by a signiture.


## Browse to find accounts

Currently the only way to look up an account is by searching for it. Since the Cafe staff is used to looking up accounts in books by first letter of an account name, we would like to give them a similar option in the UI. 

* As an alternative to using the search field, there should be a way to browse accounts in alphabetical order. 
* Currently, if you click search without entering a search string, all accounts will be displayed. If would be preferable to be explicit about this and to have a way to skip to accounts starting with a certain letter


## Outbook

Sisters is a safe space and is dedicated to maintaning a violence-free, respectful, and dignified environment in the cafe. If a customer violates the house rules, they can be put on an "out", meaning they are not invited to the cafe for some period of time. This duration is determined through a conversation with the customer and sisters staff. 

As a start to helping cafe staff identify customers who are on an out, we can show someone's out status in the barter account lookup.

* An admin user should have a way to add out status to an account. Out status should be able to be added this with an expiration date or indefinitely. 

* Counter staff should see an indicator that a customer is on out before charging their barter account for a meal. One way to do this could be to add an out badge on the search results. This could also be displayed on the main account page for a user. The indicator needs to be very bold and obvious to cafe staff


## Medical

When a customer has a medical condition that prevents them from volunteering at the Cafe, they can  spend $1.50 per day to at the cafe for free. Sometimes this lasts for a short amount of time and sometimes this is indefinite.

* An admin user should be able to enter a medical allowance for an account. A customer could have medical indefinitely or with an expiration date. Medical can only be used once a day, so the application needs to track if a customer has used medical that day. 

* Counter staff should be able to mark whether a customer has used their medical allowance that day. One possibility could be to add a medical button to the account page if that account has medical enabled. A customer should still be able to spend any barter balance that they have if they have a medical allowance.
