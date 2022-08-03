# -------- IMPORTS -------- #
# math for the percentage_change function
import math
#  requests for http requests, used to fetch data with API calls
import requests  # python -m pip install requests


# ---------- IMPORT ENVIRONMENTAL VARIABLES ---------- # 
import os
from dotenv import load_dotenv

load_dotenv()

# NEWS  -  https://newsapi.org/
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
# STOCKS  -   https://www.alphavantage.co/
ALPHA_API_KEY = os.getenv('ALPHA_API_KEY')


# ---------- OTHER VARIABLES ---------- #
# NEWS
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
COMPANY_NAME = "Tesla Inc"
# STOCKS
ALPHA_ENDPOINT = "https://www.alphavantage.co/query"
STOCK = "TSLA"
# UP_DOWN will end up being either arrow up or down depending on how our stock is moving
UP_DOWN = None


# ---------- FUNCTION TO SEE HOW MUCH A STOCK VALUE HAS CHANGED, ALSO SETS UP_DOWN ---------- #
def percentage_change(val1, val2):
    """Returns how many percent val2 has changed compared to val1.
    Floating point value, positive if val2 is higher and negative if val2 is lower
    Also changes UP_DOWN global variable to arrow up or down depending"""
    global UP_DOWN
    change = math.fabs(val1 - val2) / val1 * 100
    if val2 > val1:
        UP_DOWN = "🔺"
        return change
    else:
        UP_DOWN = "🔻"
        return - change


# --------- FUNCTION TO RETURN NEWS -------- #
def get_news(company=COMPANY_NAME, n=3):
    """Returns 3 main news-articles with company name in headline, list of dictionaries"""
    parameters = {
        # Removed parameters: "from": date, "sortBy": "popularity", "q": q,
        "qInTitle": company,
        "apiKey": NEWS_API_KEY
    }
    response = requests.get(NEWS_ENDPOINT, params=parameters)
    data = response.json()
    return data['articles'][:n]


# --------- FUNCTION TO CHECK HOW MUCH A CERTAIN STOCK HAS BEEN GOING UP OR DOWN ------- #
def stock_change(company=STOCK):
    """Returns a floating point percent value change in stock value for given company"""
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": company,
        "apikey": ALPHA_API_KEY
    }
    response = requests.get(ALPHA_ENDPOINT, params=parameters)
    response.raise_for_status()
    data = response.json()['Time Series (Daily)']
    data_list = [value for (key, value) in data.items()]    # List Comprehension
    old_value = float(data_list[1]['4. close'])    # Stock Value Day Before Yesterday
    new_value = float(data_list[0]['4. close'])    # Stock Value Yesterday
    return percentage_change(old_value, new_value)


# ---------- GENERATE OUR FINAL OUTPUT, WITH STOCK CHANGE AND 3 NEWS ARTICLES --------- #
# p is percentage change in our stock between 2 days ago and Yesterday
p = stock_change()
# articles is a list of 3 news articles, formatted as dictionaries. We are interested in ['title'] and ['description']
articles = get_news()
# Making a list of 3 news articles, formatted as strings
news_list = [f"{STOCK}: {UP_DOWN}{p:.0f}\nHeadline: {a['title']}\nBrief: {a['description']}" for a in articles]

# The original version of the program sent one SMS for each news article, using TWILIO
# Unfortunately I am not able to check that my code works since my TWILIO trial has expired
# I rather delete the code then include it unchecked.
# Feel free to sign up with TWILIO for a trial account and make this program send SMS
# For now this program will just output the articles as strings in the terminal
for n in news_list:
    print(f"{n}\n")

