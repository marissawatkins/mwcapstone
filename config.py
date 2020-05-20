import os

SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'postgres://postgres:password1@localhost:5432/capstone'
#'postgres://upkxkdyhbqlgle:1012dac3456250a1040c82e8dfbf7aece52fc79cef061e0808e49a755f56e9a4@ec2-52-71-55-81.compute-1.amazonaws.com:5432/dd20srutb23637'

SQLALCHEMY_TRACK_MODIFICATIONS = False

# bearer_tokens = {
#     ""
# }