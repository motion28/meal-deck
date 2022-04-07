import os
from urllib import response
import flask
import requests

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

app = flask.Flask(__name__)

BASE_URL = "https://api.spoonacular.com/recipes/complexSearch"
ING_URL = "https://api.spoonacular.com/recipes/"


query_params = {
    "apiKey": os.getenv("SPOON_key"),
    "query": "pasta",
    "instructionsRequired": "true",
    "addRecipeInformation": "true",
}

response = requests.get(BASE_URL, params=query_params)

# json response from API
recipes = response.json()
recipe = recipes["results"][0]
recipe_id = recipe["id"]

# Getting the ingredients for the recipe from a different URL
ingredients_touse = requests.get(
    ING_URL
    + str(recipe_id)
    + "/information?apiKey="
    + os.getenv("SPOON_key")
    + "&includeNutrition=false"
)

ingredients = ingredients_touse.json()
actual_ingredients = ingredients["extendedIngredients"]



recipe_title = recipe["title"]
recipe_image = recipe["image"]
recipe_time = recipe["readyInMinutes"]
recipe_steps = recipe["analyzedInstructions"][0]["steps"]



@app.route("/", methods=["GET", "POST"])
def all_recipes():
    """ Prints out all information for the recipe being searched """
    return flask.render_template(
        "index.html",
        recipe_title=recipe_title,
        recipe_time=recipe_time,
        recipe_image=recipe_image,
        recipe_steps=recipe_steps,
        actual_ingredients=actual_ingredients,
    )


app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)), debug=True)
