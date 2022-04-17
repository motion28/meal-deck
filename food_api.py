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
    recipe_titles = []
    recipe_images = []
    for i in range(len(data_recipes["results"])):
        result = data_recipes["results"][i]
        recipe_titles.append(result["title"])

    # container for 3 recipes
    recipe = []
    recipe2 = []
    recipe3 = []

    recipe_title = results["title"]
    recipe_title2 = results2["title"]
    recipe_title3 = results3["title"]
    # add the titles to the recipe list
    recipe.append(recipe_title)
    recipe2.append(recipe_title2)
    recipe3.append(recipe_title3)

    recipe_image = results["image"]
    recipe_image2 = results2["image"]
    recipe_image3 = results3["image"]
    # add images to the recipe list
    recipe.append(recipe_image)
    recipe2.append(recipe_image2)
    recipe3.append(recipe_image3)

    extended_ingredients = results["extendedIngredients"]
    extended_ingredients2 = results2["extendedIngredients"]
    extended_ingredients3 = results3["extendedIngredients"]

    ingredient_list = []
    ingredient_list2 = []
    ingredient_list3 = []

    # pulls ingredients and puts them in a list
    for ingredient in extended_ingredients:
        original = ingredient["original"]
        ingredient_list.append(original)

    for ingredient in extended_ingredients2:
        original = ingredient["original"]
        ingredient_list2.append(original)

    for ingredient in extended_ingredients3:
        original = ingredient["original"]
        ingredient_list3.append(original)

    # add the list of ingredients to the recipe list
    recipe.append(ingredient_list)
    recipe2.append(ingredient_list2)
    recipe3.append(ingredient_list3)

    list_analyzed_instructions = results["analyzedInstructions"]
    list_analyzed_instructions2 = results2["analyzedInstructions"]
    list_analyzed_instructions3 = results3["analyzedInstructions"]
    # containers for steps to be added below
    full_step_list = []
    full_step_list2 = []
    full_step_list3 = []
    # loops to fill list with steps
    for item in list_analyzed_instructions:
        steps = item["steps"]
        for instruction in steps:
            step = instruction["step"]
            full_step_list.append(step)
    recipe.append(full_step_list)

    for item in list_analyzed_instructions2:
        steps = item["steps"]
        for instruction in steps:
            step = instruction["step"]
            full_step_list2.append(step)
    recipe2.append(full_step_list2)

    for item in list_analyzed_instructions3:
        steps = item["steps"]
        for instruction in steps:
            step = instruction["step"]
            full_step_list3.append(step)
    recipe3.append(full_step_list3)

    full_list = [recipe, recipe2, recipe3]
    return full_list


# r = recipe_call("chicken")
# print(r[2][0])
# print(r[2][1])
# print(r[2][2])
