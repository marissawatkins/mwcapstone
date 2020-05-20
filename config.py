import os

SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'postgres://npugwmlqsehgdt:f404256bb4085249a9eb47ed884aba19cd28f3951b7c9e49799231ac27515811@ec2-52-7-39-178.compute-1.amazonaws.com:5432/d745rtq4tte8gi'
#
#postgres://postgres:password1@localhost:5432/capstone
SQLALCHEMY_TRACK_MODIFICATIONS = False

# bearer_tokens = {
#     ""
# }