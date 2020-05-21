# Capstone Project for FSND Full Stack Developer Nanodegree
## Motivation for project
My motivation for this project is to be able to put all my new skills to the test. 

## Getting Started
# Installing Dependencies
#### Python 3.7
To install Python 3.6 or Python 3.7, follow instructions from the latest python documents

#### Virtual Environment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python docs
```bash
$ cd YOUR_PROJECT_DIRECTORY_PATH/
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

#### PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to the /backend directory and running:
```bash
pip install -r requirements.txt
```
By installing requirements.txt, it will install all required packages needed

#### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

#### Database Setup
```bash
database_path = "postgres://{}:{}@{}/{}".format(<user-name>,'<password>','localhost:5432', <database_name>)"
```

#### Setting up setup.sh
After installing dependencies, execute the bash file ```setup.sh``` to set the user, Auth0 credentials and the remote db url by nagivating to the root directoy of the project and run the following command
```bash
source setup.sh
```

#### Setup Auth0
* Create an Auth0 account
* Create an application
* Create an API
* Create permissions in API. For this project, the following are the projects permissions defined within the API:
```bash
get:actor,
get:movie,
post:actor,
post:movie,
patch:actor,
patch:movie,
delete:actor,
delete:movie
```
* Define roles and attach permissions created from step above. For this project, the following roles were created:
```bash
Casting Assistant - can view actors and movies
Casting Director - All permissions a CA has, add/delete an actor from the db, modify actors/movies
Executive Producer - All permissions a CA has, add/delete a movie from the db
```

#### Setup Heroku
* Create a Heroku account
* Install heroku
* Once you have an account and Heroku installed, enter Heroku login where you can then provide your authentication information.

#### Running the server
From within the root directory first you need to make sure youre in the created virtual environment. 
To run the server, execute:
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

#### Project Steps
All endpoints written in ```bash app.py```, models in ```bash models.py```, config variable in ```bash config.py```  and all dependencies are in ```bash requirements.txt

#### Test Run
To run a test, use command ```bash python test_app.py ```.

## API Documentation and RBAC controls

castingassistant@test.com
Coffeeisgood1

castingdirector@test.com
Coffeeisgood1

execprod@test.com
Coffeeisgood1

https://{{YOUR_DOMAIN}}/authorize?audience={{API_IDENTIFIER}}&response_type=token&client_id={{YOUR_CLIENT_ID}}&redirect_uri={{YOUR_CALLBACK_URI}}

#https://mwcapstone.auth0.com/authorize?audience=mwcapstone&response_type=token&client_id=mJLgnqtDiw1gly6qpl8ScB17fiJ5wILh&redirect_uri=http://localhost:8080/login-results
make sure under applications->advanced settings->Grant types->"implicit checkbox is chcecked

create database "capstone";