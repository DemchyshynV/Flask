from flask import Flask
from config import DevConfig
from .user.views import user

app = Flask(__name__)
app.config.from_object(DevConfig)
app.register_blueprint(user)


from app import views
