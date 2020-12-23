from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

db = SQLAlchemy(app)
api = Api(app)
CORS(app)
from .resouces import ProductResource
api.add_resource(ProductResource, '/product', '/product/<int:product_id>')
