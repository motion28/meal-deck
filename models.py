import flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


app = flask.Flask(__name__)
app.secret_key = "Secret"
db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)


# class Favorites(db.Model):
# id = db.Column(db.Integer, primary_key=True)


db.create_all()
