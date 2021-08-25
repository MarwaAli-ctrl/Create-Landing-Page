# import necessary packages/modules (in this case the Flask class and config class)
from flask import Flask
from config import Config

from .site.routes import site
from .authentication.routes import auth

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db, login

from flask_login import LoginManager
#define our application as instance of the flask object
app = Flask(__name__)

# configure our application based on the config class from the config.py file

app.register_blueprint(site)
app.register_blueprint(auth)

app.config.from_object(Config)

db.init_app(app)

migrate=Migrate(app, db)

from. import models