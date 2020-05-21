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
When Postgres is running, enter the following command to create a db:
```bash CREATE DATABASE "capstone"```
Once you get your database running, enter these commands:
```bash 
        python manage.py db init
        python manage.py db migrate
        python manage.py db upgrade
```
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

* Casting Assistant - can view actors and movies
    * Permission to ```bash get:movies, get:actors```
    * Login info:
        * Email: ```bash castingassistant@test.com```
        * Password: ```bash Coffeeisgood1```
        * JWT: ```bash Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZkMC1Dc3JzQWJkcG1qQzVOZmo3dSJ9.eyJpc3MiOiJodHRwczovL213Y2Fwc3RvbmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzJkZTM5OWMwN2ExMGNlN2M3MjlmNSIsImF1ZCI6Im13Y2Fwc3RvbmUiLCJpYXQiOjE1ODk4NDEyNjksImV4cCI6MTU4OTg0ODQ2OSwiYXpwIjoibUpMZ25xdERpdzFnbHk2cXBsOFNjQjE3ZmlKNXdJTGgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.EWUxAYkMGWhbQC-7XOTcTUYvCJhTDxXNhAEUMsYkBrH1FDWV9maiIpO8v7ePCtYwcBm15DDwY0QWaR6jDP0guAom0Cor3nNIXG7nxHMgUZdL47wz3CBQeBeFlPzGNWXqFq4_CCjuAe5YXD7O11yyr-zUKMQ2cGr9HWOexrmjtho29V3cO3H6VhYjoUWaf7LKChcGd0ffoEkqtQQ22Wa4FZ91Askc3_sf_rp26rLsTACe9ETlR-G2sWZyvF8QihSCA5LV4eWxBwSL_H7mrpxTGhWgHkDGDZYG6VAepmKsfu8_uKAGBZ3blwQR54AtMX7Z5pocFTujoO45AF_usqsj0Q&expires_in=7200&token_type=Bearer```

* Casting Director - All permissions a CA has, add/delete an actor from the db, modify actors/movies
    * Permission to ```bash get:movies, get:actors, post:actors, delete:actors, patch:actors, patch:movies```
    * Login info:
        * Email: ```bash castingdirector@test.com```
        * Password: ```bash Coffeeisgood1```
        * JWT: ```bash Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZkMC1Dc3JzQWJkcG1qQzVOZmo3dSJ9.eyJpc3MiOiJodHRwczovL213Y2Fwc3RvbmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzJkZTdjOWMwN2ExMGNlN2M3MmI1NSIsImF1ZCI6Im13Y2Fwc3RvbmUiLCJpYXQiOjE1ODk4NDE0MTgsImV4cCI6MTU4OTg0ODYxOCwiYXpwIjoibUpMZ25xdERpdzFnbHk2cXBsOFNjQjE3ZmlKNXdJTGgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.ZDSa_MzTzU3_kbMd9veJHU1mIRdIcIps0t9JpIp-qsoUY2b8blxsctuy8USC1_gBVSzlKJfWJzZqLaKpXMHiWxGmcCVyKMswveCmZyWvkbaIBwty0x8sfAHDfeOKmII5qxd24yuNuOn2JL8l74Ct9zTiCG7F_5y53ApjiDrxNrmSAwj-rywpRTSc4nIUuaD9DUdJRc368q9_fQxVjbDdrUwwe1otTKi7SMRqfjpg2NmF6EGq0WV_Hn8RB69nArcJK5EYS-DtsZNV8yaJbz3SWr2pltLgLFrCw5Ltfi1T4DZiZCw9q6Jy53CNf6DI9x-PspE-XdHYJjcEQUjnQjbMnw&expires_in=7200&token_type=Bearer```

* Executive Producer - All permissions a CA has, add/delete a movie from the db
    * Permission to ```bash get:movies, get:actors```
    * Login info: ```bash get:movies, get:actors, post:actors, post:movies, delete:actors, delete:movies, patch:actors, patch:movies```
        * Email: ```bash execprod@test.com```
        * Password: ```bash Coffeeisgood1```
        * JWT: ```bash Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZkMC1Dc3JzQWJkcG1qQzVOZmo3dSJ9.eyJpc3MiOiJodHRwczovL213Y2Fwc3RvbmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzJkZWE2NmEzMDU0MGNkOTg0ZGU0MiIsImF1ZCI6Im13Y2Fwc3RvbmUiLCJpYXQiOjE1ODk4NDE2NTIsImV4cCI6MTU4OTg0ODg1MiwiYXpwIjoibUpMZ25xdERpdzFnbHk2cXBsOFNjQjE3ZmlKNXdJTGgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.f9I1x0BXRUt5qkozLTZljl6nppXhZNcWprwS5Gm8W7yjmsNBCJrqsKoGnHnWBOjuQQXa5tIcwmMmv5c8X5NjNNe9-Egzk9lzFN9GnhHp6ltInoNP0jbxB95N_5FclNTfi0SRFeJSEsfKgjDDuD5lg2yPc_jMJBrEtibuseU6smLu3jdCU39ua7_BDSwjEdU-VE1Mv_XKWe5w4AuegoFP34uXw16jfxvKux5TjlAAXJNoLr95s0WT0ThqgcidrbtllXEjgFe8-W02sasjZwdXKAnviacuTnOOUdNj_d4ksAEBEsprJ_RsejKSXflkC0BcFtGEohDm7gCxcl9HhMw9lA&expires_in=7200&token_type=Bearer```


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
All endpoints written in ```bash app.py```, models in ```bash models.py```, config variable in ```bash config.py```  and all dependencies are in ```bash requirements.txt```

#### Test Run
To run a test, use command ```bash python test_app.py ```.

#### API Documentation and RBAC controls
#### Error Handling
Errors are returned in the following way:
```bash
    return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unproccessable'
        })
```

The API will return objects when requests fail due to a certain type of condition:
```bash
    * 400: Bad Request
    * 401: Unauthorized Request
    * 404: Resource not found
    * 405: Not allowed
    * 422: Unprocessable action
    * 500: Internal error
```

### End Points
## GET '/movies
* Grabs the list of movies from db that contain a movie id, title, and release date
* Request Arguments: None
* Required permission: View actors and movies

* Sample:
    ```bash 
        {
            "movies": [
                {
                "id": 1,
                "release_data": "2020-02-20",
                "title": "Avatar"
                },
                {
                "id": 1,
                "release_data": "2020-06-06",
                "title": "Bugs Life"
                }
            ],
            "success": true
        }
    ```
## GET '/actors
* Grabs the list of movies from db that contain a actor id, name, age, and gender
* Request Arguments: None
* Required permission: View actors and movies

* Sample:
    ```bash 
        {
            "actors": [
                {
                "id": 1,
                "name": "Johnny Depp",
                "age": 54,
                "gender": "Male"
                },
                {
                "id": 5,
                "name": "Fake Person",
                "age": 4,
                "gender": "Female"
                }
            ],
            "success": true
        }
    ```

## DELETE '/movies/delete/<int:id_movies>
* Deletes details of a movie that has an id. The only users allowed to delete actors are executive producers.
* Request Arguments: id_movies, autho token
* Required permission: Add or delete movies

* Sample:
```bash
    {
        "delete": {
            "id": 4,
            "release_date": "2030-28-25",
            "title": "Fake Movie"
        }
        "success": true
    }
```

## DELETE '/actors/delete/<int:id_actor>
* Deletes details of an actor
* Request Arguments: id_actor, autho token
* Required permission: Add or delete actors

* Sample:
```bash
    {
        "delete": {
            "id": 5,
            "name": "Kate Yoko",
            "age": 25,
            "gender": "Female"
        }
        "success": true
    }
```

## POST '/actors/create
* Creates a new actor if qualified permissions are present. Casting directors and executive producers have the permission of creating a new actor
* Request Arguments: Autho token
* Required permission: View actors and movies

* Sample:
```bash
    {
        "actors": [
            {
                "id": 15,
                "name": "Jimmy Lee",
                "age": 56,
                "gender": "Male"
            },
        ], 
        "success": true
    }
```

## POST '/movies/create
* Creates a new movie if qualified permissions are present. Executive Producers are the only users that have the permission of creating a new movie
* Request Arguments: Autho token
* Required permission: Post and delete movies

* Sample:
```bash
    {
        "movies": [
            {
                "id": 15,
                "release_date": "2015-07-04",
                "title": "Lilo and Stitch"
            },
        ], 
        "success": true
    }
```

## PATCH '/actors/patch/<int:id_actor>
* Grabs the actor from db and updates correct one. Casting directors and executive producers are the only ones that can update actors
* Request Arguments: id_actor, autho token
* Required permission: Patch actors and movies

* Sample:
```bash
    {
        "actors": [
            {
                "id": 3,
                "name": "Danita Salane",
                "age": 42,
                "gender": "Female"
            },
        ], 
        "success": true
    }
```

## PATCH '/movies/patch/<int:id_movies>
* Grabs the movies from db and updates correct one. Casting directors and executive producers are the only ones that can update movies
* Request Arguments: id_movie, autho token
* Required permission: Patch actors and movies

* Sample:
```bash
    {
        "movies": [
            {
                "id": 11,
                "release_date": "2010-02-20",
                "title": "Batman"
            },
        ], 
        "success": true
    }
```

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