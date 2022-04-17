# pylint: disable=invalid-name
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member

import flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from flask_login import UserMixin


db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.Float, unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)


class Recipe(db.Model):
    __tablename__ = "Recipes"
    name = db.Column(db.String(100), primary_key=True)


class Favorite(db.Model):
    __tablename__ = "Favorites"
    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.Float, ForeignKey("Users.google_id"))
    username = db.Column(db.String(100), ForeignKey("Users.username"))
    recipe_name = db.Column(db.String(100), ForeignKey("Recipes.name"))
    # user = relationship("User", backref=backref("favorites", order_by=id))
    # favorite = relationship("Recipe", backref=backref("favorites", order_by=id))


# class Favorites(db.Model):
# id = db.Column(db.Integer, primary_key=True)
