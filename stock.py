import requests


class Stock:
    def __init__(self, yesterday, before_yesterday, parameters):
        self.yesterday_var = yesterday
        self.before_yesterday_var = before_yesterday
        self.parameter = parameters

    def get_stock(self):
        def increase_percent(price1, price2):

            crease = False
            subtracted = price1 - price2
            divided_price = subtracted / price1

            percentage = round(divided_price * 100)

            if percentage >= 5 or percentage <= -5:
                crease = True
                return crease, percentage
            else:
                return crease, percentage

        response = requests.get(url='https://www.alphavantage.co/query', params=self.parameter)
        response.raise_for_status()

        stock_data = response.json()

        yesterday_close = stock_data['Time Series (Daily)'][self.yesterday_var]['4. close']
        before_yesterday_close = stock_data['Time Series (Daily)'][self.before_yesterday_var]['4. close']

        result = increase_percent(float(yesterday_close), float(before_yesterday_close))

        return result[0], result[1]
