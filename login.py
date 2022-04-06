import os
import pathlib
import requests
import flask
from flask import session, abort, redirect, request, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from dotenv import find_dotenv, load_dotenv
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
from models import app, db, User

load_dotenv(find_dotenv())
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # set environment to HTTPS
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.unauthorized_handler
def unauthorized():
    return "You must be logged in to access this content.", 403


@login_manager.user_loader
def load_user(user_name):
    return User.query.get(user_name)


client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secrets.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=[
        "https://www.googleapis.com/auth/userinfo.profile",
        "https://www.googleapis.com/auth/userinfo.email",
        "openid",
    ],
    redirect_uri="http://127.0.0.1:5000/callback",
)


@app.route("/login")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return flask.redirect(authorization_url)


@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)
    if not session["state"] == request.args["state"]:
        abort(500)
    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID,
        clock_skew_in_seconds=10,  # allows system time to be up to 10 seconds off from server time
    )

    name = id_info.get("name")
    exists = User.query.filter_by(username=name).first()
    if not exists:
        db.session.add(User(username=name))
        db.session.commit()
    user = User.query.filter_by(username=name).first()
    login_user(user)
    return flask.redirect("/meal_deck")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return flask.redirect("/")


@app.route("/")
def index():
    return flask.render_template("login.html")


# Main portion of the app after user has logged in
@app.route("/meal_deck")
def meal_deck():
    if current_user.is_authenticated:
        return flask.render_template("mealdeck.html", username=current_user.username)
    else:
        return flask.redirect("/")


app.run()
