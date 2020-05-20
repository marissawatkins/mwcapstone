import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, create_engine
import json
from datetime import datetime
from flask_migrate import Migrate

# database_name = "capstone"
# project_direct = os.path.dirname(os.path.abspath(__file__))
# database_path =  "sqlite:///{}".format(os.path.join(project_direct, database_name))
# database_name = 'capstone'
database_path = os.environ.get('DATABASE_URL')
if not database_path:
    database_name = "capstone"
    database_path = database_path = 'postgres://srjodxxjjrwovb:7db52f15caf9edac205e47e35d7457983868a716fcbf1e3ef1b6549e4689dcaf@ec2-52-70-15-120.compute-1.amazonaws.com:5432/ddbhr7mk4qstd2'
#'postgres://postgres:Lamp,post1@localhost:5432/capstone'

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config.from_object('config')
    # app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # db = SQLAlchemy(app)
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    # db.create_all()

#-----------------MODELS----------------#

# Actor Model 
class Actor(db.Model):
    __tablename__ = 'Actor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    gender = db.Column(db.String, nullable=True)
    age = db.Column(db.Integer, nullable=True)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # def get_name(self):
    #     return self.name

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'age': self.age
        }

# Movie Model
class Movie(db.Model):
    __tablename__ = 'Movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=True)
    release_date = db.Column(db.String)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    # def get_title(self):
    #     return self.title

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }