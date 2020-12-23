class Config:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost/users_and_post'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'shjfsdl;gjlskhjgdf7chaDgsjfdjhg4jfgkhkjgsDxh2gsdfgjhfkjbhvj'


class DevConfig(Config):
    DEBUG = True
