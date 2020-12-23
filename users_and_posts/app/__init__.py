from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS

from config import DevConfig
from security import auth, identity
from .resources.user import User, UserAddPost,UserAll
from .resources.post import Post, PostById

app = Flask(__name__)
app.config.from_object(DevConfig)

api = Api(app)
jwt = JWT(app, auth, identity)

CORS(app)

api.add_resource(User, '/user', '/user/<int:user_id>')
api.add_resource(UserAddPost, '/user/<int:user_id>/post')
api.add_resource(UserAll, '/users')

api.add_resource(Post, '/posts')
api.add_resource(PostById, '/post/<int:post_id>')
