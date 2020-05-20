import os

SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'postgres://ahiowinkqhmxhm:5156e97ad8c9bc51844b9b46f40c75ce639cc0b11508c3f46f25d3e6599173bc@ec2-52-207-93-32.compute-1.amazonaws.com:5432/d3p52lr6dlv66'
#
#postgres://postgres:password1@localhost:5432/capstone
SQLALCHEMY_TRACK_MODIFICATIONS = False

# bearer_tokens = {
#     ""
# }