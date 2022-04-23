# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-error
# pylint: disable=E0202

import unittest
import pathlib
import sys
import os
from unittest.mock import patch
import flask_unittest
from main import load_user
from main import meal_deck, login, callback, logout, index, get_food, add_favorite, add_plan, delete_favorite, delete_plan, get_favorites, get_plan
from dotenv import find_dotenv, load_dotenv
from main import get_food
from models import User


current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

INPUT = "INPUT"
EXP_OUTPUT = "EXP_OUTPUT"


class test_Get_food(unittest.TestCase):
    """
    This class contains the test cases for the get_food function"""

    def test_get_food(self):
        """
        This test will check if the function returns the correct food
        """
        self.success_test_params = [
            {
                INPUT: "",
                EXP_OUTPUT: {
                    "title": "",
                    "imageURL": "",
                    "extendedIngredients": "[]",
                    "analyzedInstructions": "[]",
                },
            },
            {
                INPUT: "apple",
                EXP_OUTPUT: {
                    "title": "Apple",
                    "imageURL": "https://spoonacular.com/recipeImages/apple-pie-9-636894.jpg",
                    "extendedIngredients": "1 apple",
                    "analyzedInstructions": "[]",
                },
            },
            {
                INPUT: "pasta",
                EXP_OUTPUT: {
                    "title": "Pasta with Garlic, Scallions, Cauliflower & Breadcrumbs",
                    "imageURL": "https://spoonacular.com/recipeImages/pasta-with-garlic-scallions-cauliflower-breadcrumbs-7-636894.jpg",
                    "extendedIngredients": "1/2 cup olive oil, 1/2 cup chopped fresh parsley, 1/2 cup chopped fresh chives, 1/2 cup chopped fresh garlic, 1/2 cup chopped fresh oregano, 1/2 cup chopped fresh basil, 1/2 cup chopped fresh thyme, 1/2 cup chopped fresh rosemary, 1/2 cup chopped fresh fennel, 1/2 cup chopped fresh parsley, 1/2 cup chopped fresh chives, 1/2 cup chopped fresh garlic, 1/2 cup chopped fresh oregano, 1/2 cup chopped fresh basil, 1/2 cup chopped fresh thyme, 1/2 cup chopped fresh rosemary, 1/2 cup chopped fresh fennel, 1/2 cup chopped fresh parsley, 1/2 cup chopped fresh chives, 1/2 cup chopped fresh garlic, 1/2 cup chopped fresh oregano, 1/2 cup chopped fresh basil, 1/2 cup chopped fresh thyme, 1/2 cup chopped fresh rosemary, 1/2 cup chopped fresh fennel, 1/2 cup chopped fresh parsley, 1/2 cup chopped fresh chives, 1/2 cup chopped fresh garlic, 1/2 cup chopped fresh oregano, 1/2 cup chopped fresh basil, 1/2 cup chopped fresh thyme, 1/2 cup chopped fresh rosemary, 1/2 cup chopped fresh fennel, 1/2 cup chopped fresh parsley, 1/2 cup chopped fresh chives, 1/2 cup chopped fresh garlic, 1/2 cup chopped fresh oregano, 1/2 cup chopped fresh basil, 1/2 cup chopped fresh thyme, 1/2 cup chopped fresh rosemary, 1/2 cup chopped fresh fennel, 1/2 cup chopped fresh parsley, 1/2 cup chopped fresh chives, 1/2 cup chopped fresh garlic, 1/2 cup chopped fresh oregano, 1/2 cup chopped fresh basil, 1/2 cup chopped fresh thyme, 1/2 cup chopped fresh rosemary, 1/2 cup chopped fresh fennel, 1/2 cup chopped fresh parsley",
                    "analyzedInstructions": "In a large skillet, melt butter over medium heat until foamy. Then add bread crumbs, tossing to coat in butter, until toasted and lightly browned. Remove from pan into small bowl; mix in cheese and about a tablespoon of the green scallion tops.",
                },
            },
            {
                INPUT: "pasta",
                EXP_OUTPUT: {
                    "title": "Pasta with Tuna ",
                    "id": "654959",
                    "imageURL": "https://spoonacular.com/recipeImages/pasta-with-tuna-654959.jpg",
                    "extendedIngredients": "2 Tablesspoons Flour, 1 cup Green Onions chopped, 1 1/4 cups Non-Fat Milk, 2 tablespoons Olive Oil, 2 tablespoons Onions minced, 1/4 cup Parmesan Cheese grated, 1 cup Fresh Parsley or Basil chopped, 8 ounces Tubular Pasta, 1 cup Frozen Peas thawed, 1 dish Hot Pepper Sauce, 6 1/2 ounces Can Water-Packed Tuna drained",
                    "analyzedInstructions": "Cook pasta in a large pot of boiling water until al dente. Drain and return to warm pot. Put olive oil in saucepan and add onion. Saute until transparent. Stir in flour and cook for a few seconds and then whisk in milk. Stir constantly until this thickens. Add peas, tuna (shredded into chunks,) parsley, green onions, cheese and hot pepper sauce. Pour over pasta and stir gently to mix. Serve at once.",
                },
            },
            {
                INPUT: "bread, fish",
                EXP_OUTPUT: {
                    "title": "",
                    "imageURL": "",
                    "extendedIngredients": "",
                    "analyzedInstructions": "",
                },
            },
            {
                INPUT: "1111",
                EXP_OUTPUT: {
                    "title": "",
                    "imageURL": "",
                    "extendedIngredients": "",
                    "analyzedInstructions": "",
                },
            },
            {
                INPUT: "8",
                EXP_OUTPUT: {
                    "title": "",
                    "imageURL": "",
                    "extendedIngredients": "",
                    "analyzedInstructions": "",
                },
            },
        ]

        for test_params in self.success_test_params:
            with patch("main.get_food") as mock_get_food:
                mock_get_food.return_value = test_params[EXP_OUTPUT]
                self.assertEqual(get_food(), test_params[EXP_OUTPUT])

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


class test_main_py(unittest.TestCase):
    """
    This test will check existence of client_secrets.json and tests if envhas all the variables
    """

    def client_secrets_exists(self):
        """Reads the client_secrets.json file and checks if it exists"""
        secretsPath = os.path.join(pathlib.Path(__file__).parent, "client_secrets.json")
        return bool(os.path.exists(secretsPath))

    def env_test(self):
        """This function tests if the environment variables are set"""
        load_dotenv(find_dotenv())
        spoon_exists = os.getenv("SPOON_key")
        client_id_exists = os.getenv("GOOGLE_CLIENT_ID")
        client_secret_exists = os.getenv("GOOGLE_CLIENT_SECRET")
        secret_key_exists = os.getenv("secret_key")
        session_key_exists = os.getenv("session_key")
        self.assertNotEqual(spoon_exists, None)
        self.assertNotEqual(client_id_exists, None)
        self.assertNotEqual(client_secret_exists, None)
        self.assertNotEqual(secret_key_exists, None)
        self.assertNotEqual(session_key_exists, None)

    if __name__ == "__main__":
        unittest.main()


class TestFoo(flask_unittest.ClientTestCase):
    app = meal_deck()
    def setUp(self, client):
        pass

    def tearDown(self, client):
        pass

    def test_foo_with_client(self, client):
        # Use the client here
        check = client.get('/hello')
        self.assertInResponse(check, 'hello world!')
    
    if __name__ == '__main__':
        unittest.main()

class TestFoo1(flask_unittest.ClientTestCase):
    app = login()
    def setUp(self, client):
        pass

    def tearDown(self, client):
        pass

    def test_foo_with_client(self, client):
        # Use the client here
        check = client.get('/hello')
        self.assertInResponse(check, 'hello world!')
    if __name__ == '__main__':
        unittest.main()

class TestFoo2(flask_unittest.ClientTestCase):
    app = index()
    def setUp(self, client):
        pass

    def tearDown(self, client):
        pass

    def test_foo_with_client(self, client):
        # Use the client here
        check = client.get('/hello')
        self.assertInResponse(check, 'hello world!')
    if __name__ == '__main__':
        unittest.main()

class TestFoo3(flask_unittest.ClientTestCase):
    app = index()
    def setUp(self, client):
        pass

    def tearDown(self, client):
        pass

    def test_foo_with_client(self, client):
        # Use the client here
        check = client.get('/hello')
        self.assertInResponse(check, 'hello world!')
    if __name__ == '__main__':
        unittest.main()

class TestFoo4(flask_unittest.ClientTestCase):
    app = get_food()
    def setUp(self, client):
        pass

    def tearDown(self, client):
        pass

    def test_foo_with_client(self, client):
        # Use the client here
        check = client.get('/hello')
        self.assertInResponse(check, 'hello world!')
    if __name__ == '__main__':
        unittest.main()

class TestFoo5(flask_unittest.ClientTestCase):
    app = add_favorite()
    def setUp(self, client):
        pass

    def tearDown(self, client):
        pass

    def test_foo_with_client(self, client):
        # Use the client here
        check = client.get('/hello')
        self.assertInResponse(check, 'hello world!')
    if __name__ == '__main__':
        unittest.main()

class TestFoo6(flask_unittest.ClientTestCase):
    app = add_plan()
    def setUp(self, client):
        pass

    def tearDown(self, client):
        pass

    def test_foo_with_client(self, client):
        # Use the client here
        check = client.get('/hello')
        self.assertInResponse(check, 'hello world!')
    if __name__ == '__main__':
        unittest.main()

class TestFoo7(flask_unittest.ClientTestCase):
    app = delete_favorite()
    def setUp(self, client):
        pass

    def tearDown(self, client):
        pass

    def test_foo_with_client(self, client):
        # Use the client here
        check = client.get('/hello')
        self.assertInResponse(check, 'hello world!')
    if __name__ == '__main__':
        unittest.main()

class TestFoo8(flask_unittest.ClientTestCase):
    app = delete_plan()
    def setUp(self, client):
        pass

    def tearDown(self, client):
        pass

    def test_foo_with_client(self, client):
        # Use the client here
        check = client.get('/hello')
        self.assertInResponse(check, 'hello world!')
    if __name__ == '__main__':
        unittest.main()

class TestFoo9(flask_unittest.ClientTestCase):
    app = get_favorites()
    def setUp(self, client):
        pass

    def tearDown(self, client):
        pass

    def test_foo_with_client(self, client):
        # Use the client here
        check = client.get('/hello')
        self.assertInResponse(check, 'hello world!')
    if __name__ == '__main__':
        unittest.main()

class TestFoo10(flask_unittest.ClientTestCase):
    app = get_plan()
    def setUp(self, client):
        pass

    def tearDown(self, client):
        pass

    def test_foo_with_client(self, client):
        # Use the client here
        check = client.get('/hello')
        self.assertInResponse(check, 'hello world!')
    if __name__ == '__main__':
        unittest.main()