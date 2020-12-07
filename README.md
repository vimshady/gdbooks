# gdbooks

To run the server locally
- create virtual environment`python3 -m venv gdenv`
- launch it `source gdenv/bin/activate`
- install requirements from basefolder `pip install requirements.txt`
- run database migration `python manage.py migrate`
- run django local server `python manage.py runserver`


I was able to impement the list all requests and specific requests endpoints as well as delete a request endpoint but tripped up on the create request endpoint. I wasn't able to pull in data from the request context in order to validate email and book titles. That's what I would've done next.

I'm disappointed I didn't complete the assignment but grateful for this opportunity.