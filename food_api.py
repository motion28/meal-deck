# pylint: disable=invalid-name
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member
# pylint: disable=line-too-long

import os
import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


def recipe_call(search_term):
    """
    uses search term and returns most popular result (1, can be modified in url at the end '&number=').
    returns results only containing an ingredients list and cooking instructions
    """
    RECIPE_API_KEY = os.getenv("SPOON_key")

    url = f"https://api.spoonacular.com/recipes/complexSearch?query={search_term}&apiKey={RECIPE_API_KEY}&addRecipeInformation=True&fillIngredients=True&number=3"
    data_recipes = requests.get(url).json()
    num_of_results = len(data_recipes["results"])

    recipe_titles = []
    recipe_images = []
    extended_ingredients = []
    ingredients = [[]] * num_of_results
    analyzed_instructions = []
    instructions = [[]] * num_of_results

    for i in range(num_of_results):
        result = data_recipes["results"][i]
        recipe_titles.append(result["title"])
        recipe_images.append(result["image"])
        extended_ingredients.append(result["extendedIngredients"])
        analyzed_instructions.append(result["analyzedInstructions"])

    # pulls ingredients and puts them in a list
    for i in range(num_of_results):
        for ingredient in extended_ingredients[i]:
            original = ingredient["original"]
            ingredients[i].append(original)

    # loops to fill list with steps
    for i in range(num_of_results):
        for item in analyzed_instructions[i]:
            steps = item["steps"]
            for instruction in steps:
                step = instruction["step"]
                instructions[i].append(step)

    return (recipe_titles, recipe_images, ingredients, instructions)


# r = recipe_call("chicken")
# print(r[2][0])
# print(r[2][1])
# print(r[2][2])
