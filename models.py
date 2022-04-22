# pylint: disable=invalid-name
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member
# pylint: disable=import-error
# pylint: disable=too-few-public-methods

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask_login import UserMixin


db = SQLAlchemy()

# User table
class User(db.Model, UserMixin):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.Float, unique=True, nullable=False)
    username = db.Column(db.String(100), unique=False, nullable=False)


# Favorite recipes table
class Favorite(db.Model):
    __tablename__ = "Favorites"
    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.Float, ForeignKey("Users.google_id"))
    recipe_name = db.Column(db.String(100))  # store recipe name


# Meal plan table
class Plan(db.Model):
    __tablename__ = "Plan"
    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.Float, ForeignKey("Users.google_id"))
    day = db.Column(db.String(80)) # store day of the week
    recipe_name = db.Column(db.String(100))  # store recipe name
