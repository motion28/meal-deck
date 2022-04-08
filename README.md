**CSC 4350 Spring 2022 Final Project Sprint 1**

**MealDeck** by Moumin Ali, Augustine Li, Nestor Kaputo, and Kirtan Kabariya

**Heroku Deployment:**

## Setup Instructions
1. To install required libraries for Visual Studio Code, type the following command in the terminal:
`pip3 install -r requirements.txt`
2. To setup this program for running, we need **Google Client** and **Spoonacular API** prepared:

**Google Client Setup:**
To setup Google Client, first create a Google account if you don't have one.
Then, go to https://console.developers.google.com/apis/credentials
and login with your account.
Agree to the terms of service if prompted.
Then, click on Create credentials,
and select OAuth client ID in the dropdown options.

Then, select Web application option.
Then, go to Authorized redirect URIs,
and add the following url:
http://127.0.0.1:5000/callback

Now, you can see client ID key/link.

**Spoonacular API setup:**
Sign up for Spoonacular here: https://spoonacular.com/food-api/console#Dashboard
Create your account and then get your spoonacular key.

With all the keys ready, create a `.env` file in the top directory
and TYPE out the keys WITH quotation marks in an `.env` file
```
SPOON_key="insert your SPOONACULAR key"
GOOGLE_CLIENT_ID="insert your GOOGLE CLIENT key"
secret_key="insert ANYTHING you want"
session_key="insert ANYTHING you want"
```

## To Run MealDeck
Run the following command in VSCode Terminal:
`python3 main.py` 