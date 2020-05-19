import os

SECRET_KEY = urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'postgres://srjodxxjjrwovb:7db52f15caf9edac205e47e35d7457983868a716fcbf1e3ef1b6549e4689dcaf@ec2-52-70-15-120.compute-1.amazonaws.com:5432/ddbhr7mk4qstd2'

SQLALCHEMY_TRACK_MODIFICATIONS = False

# bearer_tokens = {
#     ""
# }