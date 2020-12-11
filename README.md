# gdbooks

To run the server locally
- create virtual environment (e.g. `python3 -m venv gdenv`)
- launch it (e.g. `source gdenv/bin/activate`)
- install requirements from basefolder `pip install requirements.txt`
- run database migration `python manage.py migrate`
- run django local server `python manage.py runserver`

## Endpoints:

### Create request:

`POST /request`

Example request body:
```JSON
{
    "email": "jake@jake.jake",
    "title": "War and Peace",
}
```

No authentication required

Required fields: `email`, `title`


### Get request list:

`GET /request/`

No authentication required

### Get specific request:

`GET /request/:id`

No authentication required

### Delete request:

`DELETE /request/:id`

No authentication required


## Available Library Books
- Blink
- Delivering Happiness
- The War on Normal People
- Radical Markets
- Progress and Poverty
- Development as Freedom
- Banker to the Poor by
- Crime and Punishment
- The Sound and Fury
- War and Peace
- Pride and Prejudice