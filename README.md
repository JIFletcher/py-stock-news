# Stock News
A simple exercise in use of API's.

This program takes your stock of interest and checks how much the stock has been moving up or down during Yesterday.
The original idea was that the program would run early in the morning and check whether your stock had been moving a lot, if it had the program would notify you on SMS and also include the main 3 headlines about your stock.

This version of the program does not do a check on how much the stock has been moving.

Also I disbanded the SMS functionality, since my trial with TWILIO has ended and I am not very keen on spending money.

Unfortunately I did not manage to find any "free forever" SMS service, which makes SMS integraton pointless for my purposes. But please feel free to experiment, there is an excellent article here:

[https://www.courier.com/guides/python-send-sms/](https://www.courier.com/guides/python-send-sms/)

That articles mentions 4 alternatives:
1. Twilio API
2. Vonage API
3. Plivo API
4. Multi-Channel Notification API

Once you master how to use API (understand the rest of the code in this project), SMS integration is very simple, but seemingly never free past trial periods.

This version of the program just outputs text strings in the console, instead of sending any SMS.

I could integrate email-support, but thought it would be nice to let current version be a simple project to study for anyone starting up with API's, so I try to keep it basic.

---

## 100 Days of python
This game was written as an assignment on day 36 (of 100) in an excellent programming class led by brilliant educator Dr. Angela Yu.
The class is available for purchase on the online educational platform udemy:

[100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)

---

## Version(s)
v1.0.0 The original assignment (SMS support removed)

----

## Future plans?
I don't have a current interest in stocks, but I could possibly make a version of this program that checks on my cryptos (if they ever regain any value - written 3. august 2022)

---

## API-keys
To be able to use this code you need your own API keys from two different sites:

[https://www.alphavantage.co/](https://www.alphavantage.co/)

[https://newsapi.org/](https://newsapi.org/)

It is easy and straightforward to acquire API keys from these websites.

---

## Environmental variables

API-keys are secrets, never let anyone else see them, you hide them in a file you call `.env`

Make the file with the following terminal command: `touch .env`

You can edit the file in a number of ways. Consult a guide on how to set up terminal with your favorite editor. I use Visual Studio Code. I have set it up so I write the following to edit .env : `code .env`

Content of .env :

```
NEWS_API_KEY = "paste_your_news_api_here"
ALPHA_API_KEY = "paste_your_stock_api_here"
```

For understanding, read this article:

[https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1](https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1)


---

## Running the code
To run the code of the project, please first get your own API keys and follow these instructions:

1. Start your terminal (bash)
2. Make sure you have git installed: `git --version`
3. `cd` into whatever folder you want the project in
4. Make sure you are not already in a git repo: `git status`
5. Clone the project onto your local machine: `git clone <github url>`
6. cd into the project folder: `cd py-stock-news`
7. Make your .env file (as described above)
8. Run the project: `python main.py`

---

## License
The code is published under the MIT license. That basically means that you are free to use the code as you please. Read the LICENSE file for more info.