from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restless import APIManager
from flask_cors import CORS
import os

# --- Database Connection Info --- #
class Config (object):
    SQLALCHEMY_DATABASE_URI = "postgresql://posts:postspassword@posts.cbryqhibnhym.us-east-1.rds.amazonaws.com:5432/posts"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

