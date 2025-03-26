import os

class Config:
    SQLALCHEMY_DATABASE_URI ='sqlite:///../instance/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY','supersecretkey')

class TestingConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI ='sqlite:///:memory:'
    SECRET_KEY = os.getenv('SECRET_KEY','supersecretkey')
    WTF_CSRF_ENABLED = False
    LOGIN_DISABLED = True