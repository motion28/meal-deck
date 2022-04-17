# pylint: disable=invalid-name
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member

import flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.Float, unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)


# class Favorites(db.Model):
# id = db.Column(db.Integer, primary_key=True)
