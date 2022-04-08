import unittest
from unittest.mock import MagicMock, patch
from main import get_food
from login import load_user
from models import User
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

INPUT = "INPUT"
EXP_OUTPUT = "EXP_OUTPUT"


class test_get_food(unittest.TestCase):
   
    def test_get_food(self):
        """
        This test will check if the function returns the correct food
        """
        self.success_test_params = [
            {
            INPUT: "",
            EXP_OUTPUT: {'title':'','id':'', 'imageURL':'', 'extendedIngredients':'', 'analyzedInstructions':''}
            },
            {
            INPUT: "apple",
            EXP_OUTPUT: {'title':'Apple','id':'1','imageURL':'https://spoonacular.com/recipeImages/apple-pie-9-636894.jpg','extendedIngredients':'1 apple', 'analyzedInstructions': '[]'},
            },
            {
            INPUT: "pasta",
            EXP_OUTPUT: {'title':'Pasta with Garlic, Scallions, Cauliflower & Breadcrumbs','id': '716429','imageURL':'https://spoonacular.com/recipeImages/pasta-with-garlic-scallions-cauliflower-breadcrumbs-7-636894.jpg','extendedIngredients':'1/2 cup olive oil, 1/2 cup chopped fresh parsley, 1/2 cup chopped fresh chives, 1/2 cup chopped fresh garlic, 1/2 cup chopped fresh oregano, 1/2 cup chopped fresh basil, 1/2 cup chopped fresh thyme, 1/2 cup chopped fresh rosemary, 1/2 cup chopped fresh fennel, 1/2 cup chopped fresh parsley, 1/2 cup chopped fresh chives, 1/2 cup chopped fresh garlic, 1/2 cup chopped fresh oregano, 1/2 cup chopped fresh basil, 1/2 cup chopped fresh thyme, 1/2 cup chopped fresh rosemary, 1/2 cup chopped fresh fennel, 1/2 cup chopped fresh parsley, 1/2 cup chopped fresh chives, 1/2 cup chopped fresh garlic, 1/2 cup chopped fresh oregano, 1/2 cup chopped fresh basil, 1/2 cup chopped fresh thyme, 1/2 cup chopped fresh rosemary, 1/2 cup chopped fresh fennel, 1/2 cup chopped fresh parsley, 1/2 cup chopped fresh chives, 1/2 cup chopped fresh garlic, 1/2 cup chopped fresh oregano, 1/2 cup chopped fresh basil, 1/2 cup chopped fresh thyme, 1/2 cup chopped fresh rosemary, 1/2 cup chopped fresh fennel, 1/2 cup chopped fresh parsley, 1/2 cup chopped fresh chives, 1/2 cup chopped fresh garlic, 1/2 cup chopped fresh oregano, 1/2 cup chopped fresh basil, 1/2 cup chopped fresh thyme, 1/2 cup chopped fresh rosemary, 1/2 cup chopped fresh fennel, 1/2 cup chopped fresh parsley, 1/2 cup chopped fresh chives, 1/2 cup chopped fresh garlic, 1/2 cup chopped fresh oregano, 1/2 cup chopped fresh basil, 1/2 cup chopped fresh thyme, 1/2 cup chopped fresh rosemary, 1/2 cup chopped fresh fennel, 1/2 cup chopped fresh parsley', 'analyzedInstructions': 'In a large skillet, melt butter over medium heat until foamy. Then add bread crumbs, tossing to coat in butter, until toasted and lightly browned. Remove from pan into small bowl; mix in cheese and about a tablespoon of the green scallion tops.'},
            },
            {
            INPUT: "pasta",
            EXP_OUTPUT: {'title': 'Pasta with Tuna ', 'id':'654959', 'imageURL':'https://spoonacular.com/recipeImages/pasta-with-tuna-654959.jpg', 'extendedIngredients':'2 Tablesspoons Flour, 1 cup Green Onions chopped, 1 1/4 cups Non-Fat Milk, 2 tablespoons Olive Oil, 2 tablespoons Onions minced, 1/4 cup Parmesan Cheese grated, 1 cup Fresh Parsley or Basil chopped, 8 ounces Tubular Pasta, 1 cup Frozen Peas thawed, 1 dish Hot Pepper Sauce, 6 1/2 ounces Can Water-Packed Tuna drained',  'analyzedInstructions': 'Cook pasta in a large pot of boiling water until al dente. Drain and return to warm pot. Put olive oil in saucepan and add onion. Saute until transparent. Stir in flour and cook for a few seconds and then whisk in milk. Stir constantly until this thickens. Add peas, tuna (shredded into chunks,) parsley, green onions, cheese and hot pepper sauce. Pour over pasta and stir gently to mix. Serve at once.'},
            },
            {
            INPUT: '1111',
            EXP_OUTPUT: {'title':'','id':'','imageURL':'','extendedIngredients':'','analyzedInstructions':''},
            },
        ]

        for test_params in self.success_test_params:
            with patch('main.get_food') as mock_get_food:
                mock_get_food.return_value = test_params[EXP_OUTPUT]
                self.assertEqual(get_food(test_params[INPUT]), test_params[EXP_OUTPUT])
        

        
        # Set up the test
        food = get_food()
        # Run the test
        self.assertEqual(food, "pizza")

    # Test the load_user function
    def test_load_user(self):
        """
        This test will check if the function returns the correct user
        """
        # Set up the test
        user = load_user(User.username)
        # Run the test
        self.assertEqual(user, "user")
    
    
    if __name__ == "__main__":
        unittest.main()