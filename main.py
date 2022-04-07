import os
import flask
import food_api

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/get-food')
def get_food():
    search_input = flask.request.args.get('food_input').lower()
    search_term = str(search_input)
    food_recipe = food_api.recipe_call(search_input)

    recipe_title = food_recipe[0][0]
    recipe_image = food_recipe[0][1]
    recipe_ingredients = food_recipe[0][2]
    recipe_instructions = food_recipe[0][3]

    recipe_title2 = food_recipe[1][0]
    recipe_image2 = food_recipe[1][1]
    recipe_ingredients2 = food_recipe[1][2]
    recipe_instructions2 = food_recipe[1][3]

    recipe_title3 = food_recipe[2][0]
    recipe_image3 = food_recipe[2][1]
    recipe_ingredients3 = food_recipe[2][2]
    recipe_instructions3 = food_recipe[2][3]

    
    return flask.render_template(
        'food.html',
        search_term=search_term, 
        recipe_title=recipe_title,
        recipe_image=recipe_image,
        recipe_ingredients=recipe_ingredients, 
        recipe_instructions=recipe_instructions,
        recipe_title2=recipe_title2,
        recipe_image2=recipe_image2,
        recipe_ingredients2=recipe_ingredients2, 
        recipe_instructions2=recipe_instructions2,
        recipe_title3=recipe_title3,
        recipe_image3=recipe_image3,
        recipe_ingredients3=recipe_ingredients3, 
        recipe_instructions3=recipe_instructions3,
        search_success=True
    )


app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)), debug=True)
