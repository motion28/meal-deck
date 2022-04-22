**CSC 4350 Spring 2022 Final Project Sprint 1**

**MealDeck** by Moumin Ali, Augustine Li, Nestor Kaputo, and Kirtan Kabariya

**Heroku Deployment: https://rocky-basin-61067.herokuapp.com/**

If you get an url error when trying to log in via google, press back and try again. Sometimes Google API is slow for some reason.


## Setup Instructions
1. To install required libraries for Visual Studio Code, type the following command in the terminal:
`pip3 install -r requirements.txt`
2. To setup this program for running, we need **Google Client** and **Spoonacular API** prepared:
3. If you wish to test locally change the value of `redirect_uri` in line 99 of `main.py` to http://127.0.0.1:5000/callback. As well as uncomment line 356 and comment line 360 and 361.


**We need to setup .env file**

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

Now, you can see your Google client ID key/link as well as your Google client secret.

**Spoonacular API setup:**
Sign up for Spoonacular here: https://spoonacular.com/food-api/console#Dashboard
Create your account and then get your spoonacular key.

**.env Setup:**
With all the keys ready, create a `.env` file in the top directory
and TYPE out the keys WITH quotation marks in an `.env` file
```
SPOON_key="Insert your SPOONACULAR key"
GOOGLE_CLIENT_ID="Insert your GOOGLE CLIENT key"
secret_key="Insert ANYTHING you want"
session_key="Insert ANYTHING you want"
```

## To Run MealDeck
Run the following command in VSCode Terminal:
`python3 main.py` 
In the login page, clicking login will prompt you to login to a Google account, if you are not already logged in.

If you don't have an account, the app creates it for you. If you do, you are logged in.

Then, you can search for food items in the app.

## Troubleshooting
**ValueError: Token used too early/Token used too late issue**
This issue occurs when your system time is out of sync with Google Servers.
One possible solution is to re-sync the system time: https://www.groovypost.com/howto/synchronize-clock-windows-10-with-internet-atomic-time/

Another solution is to increase the clock skew tolerance. 
To do that, go to **main.py** and find `clock_skew_in_seconds`, and increase that value.
