# Song Streamer
A project to enable streaming personal music securely

## Requirements
- python3
- pip3
- virtualenv

For Linux based systems with `apt` you can do:
- `sudo apt-get install python3`
- `sudo pip3 install virtualenv`

## Setup
- Navigate to root of project
- Create a virtualenv `virtualenv -p python3 env`
- Activate it `source env/bin/activate`
- Install dependencies with pip `pip install -r requirements.txt`

## Run server
- [Setup your environment](#setup)
- Navigate to django project root `cd songstreamer`
- Run the migrations `python manage.py migrate`
- Run a local server `python manage.py runserver`
- Open a browser and navigate to `http://localhost:8000`

## Run tests
- [Setup your environment](#setup)
- Run pytest `py.test`
