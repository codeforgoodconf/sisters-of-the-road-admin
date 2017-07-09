# barter
People's credits for food / volunteering

## MVP (to work on during event)
- keep track of customers' credit balance as they volunteer and get meals
- customers' balances can go up as they volunteer time
- customers' balances can go down as they get meals
- POS client target is a tablet; one will be furnished for testing during development
- database needs to be encrypted
- ensure legibility with large fonts
- special login for POS user, use permissions system
- client / customer
  - find customer
  - display balance
  - enter total, mark add or subtract
  - save, recording the date and time
- admin side
  - add/remove customers 
  - search for customer 
  - view all customers
  - view credit balance for customer
  - see log of how credits were used

## MVP+1 (for the future)
- signature verification with javascript (see Ruby For Good 2016 habitat for
  humanity project, should have reusable code)
- firewall to only access site from cafe wifi

## MVP+2 (for the far future)
- integrate with register
- keep track of item by item
- integrate with outbox
- integrate with medical

# medical (for the future)
separate barter log for people who get a $1.50 credit per day bc they can't do
physical volunteering

- permanent medical folks get 1.50 a day; non-cumulative.
- temporary medical has an end date; still get 1.50 a day non cumulative.
- both need notes
  see that folks have medical exception when searched on the POS and display slightly different UI

# outbook (for the future)
Tracks incidents with customers and volunteers
- a report has customers
- multiple people add notes to report
- track the point person -- they made the report / decided on the out
- date of event
- welcome back date
- check that incident was reported
- show in user list who is out
- show in POS interface that someone is out -- mention point person / wb date

