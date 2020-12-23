from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from config import DevConfig
from app.resources import User
from security import authenticate, identity

app = Flask(__name__)
app.config.from_object(DevConfig)

jwt = JWT(app, authenticate, identity) #/auth
api = Api(app)

api.add_resource(User, '/user', '/user/<string:email>')
