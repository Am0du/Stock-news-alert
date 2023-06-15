
import os
import datetime as dt
from twilio.rest import Client
from stock import Stock
from news import News


today_date = dt.date.today()
yesterday_date = today_date - dt.timedelta(days=1)
formatted_yesterday = yesterday_date.strftime('%y-%m-%d')

before_yesterday = yesterday_date - dt.timedelta(days=1)
formatted_before_yesterday = before_yesterday.strftime('%y-%m-%d')


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

news_params = {
    'apiKey': os.environ.get('News_api'),
    'q': COMPANY_NAME,
    'from': formatted_before_yesterday,
    'to': formatted_yesterday,
    'sortBy': 'popularity'
}

alphavantage_params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'apikey': os.environ.get('API_key')
}

stock = Stock(formatted_yesterday,formatted_before_yesterday,alphavantage_params)

stocks = stock.get_stock()

if stocks[0]:
    percent = stocks[1]
    if percent < 0:
        percent = str(percent)
        percent = percent.replace('-', '')
        new_percent = '🔻'+f'{percent}'
    else:
        percent = str(percent)
        new_percent = '🔺' + f'{percent}'

    news = News(news_params)
    relevant_news = news.top_three
    for i in relevant_news:
        acc_sid = os.environ.get('Twillio_sid')
        auth_tok = os.environ.get('Twillio_api')
        client = Client(acc_sid, auth_tok)

        message = client.messages.create(
            body=f"{STOCK}: {new_percent}\n\nHeadline: {i['title']}\n\nBrief: {i['description']}\n\nUrl: {i['url']}",
            from_='+14066434554',
            to='+234810429666'
        )

