import os
from urllib import response
import flask
import requests

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

app = flask.Flask(__name__)

BASE_URL = "https://api.spoonacular.com/recipes/complexSearch"


query_params = {
    "apiKey": os.getenv("SPOON_key"),
    "query": "chicken",
    "number": "5",
    "instructionsRequired": "true",
    "addRecipeInformation": "true",
}

response = requests.get(BASE_URL, params=query_params)

# json response from API
recipes = response.json()


recipe = recipes["results"][0]
recipe_id = recipe["id"]
recipe_title = recipe["title"]

recipe_image = recipe["image"]

# recipe_sum = recipe["summary"]


@app.route("/")
def index():
    return flask.render_template(
        "index.html",
        recipe=recipe,
        recipe_title=recipe_title,
        recipe_image=recipe_image,
        # recipe_sum=recipe_sum,
    )


app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)), debug=True)
