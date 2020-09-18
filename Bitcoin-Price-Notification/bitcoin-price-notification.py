from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from datetime import datetime
import requests
import json


class bitcoinPriceNotification:
    def __init__(self):
        self.THRESHOLD_AMOUNT = 10000
        self.IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{}/with/key/p0rfyWkMTm3LiTEQ34dhS8VKzyHTGsAPhmF4nDvfZnq'

    def get_latest_bitcoin_price(self):

        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
            'start': '1',
            'limit': '5000',
            'convert': 'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '37fa82a6-5d7c-407f-8ae1-6b1e46d64c23',
        }
        session = Session()
        session.headers.update(headers)
        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
        # Convert the price to a floating point number
        return float(data['data'][0]['quote']['USD']['price'])

    # requesting the notification from IFTTT
    def post_ifttt_webhook(self, event, value):
        data = {'value1': value}
        ifttt_event_url = self.IFTTT_WEBHOOKS_URL.format(event)
        requests.post(ifttt_event_url, json=data)

    # Formats the date into a string: '24.02.2018 15:09'
    def bitcoin_history(self, bitcoin_history):
        rows = []
        for bitcoin_price in bitcoin_history:
            date = bitcoin_price['date'].strftime('%d.%m.%Y %H:%M')
            price = bitcoin_price['price']
            row = '{}: $<b>{}</b>'.format(date, price)
            rows.append(row)
        return '<br>'.join(rows)

    def main(self):
        bitcoinHistory = []
        price = self.get_latest_bitcoin_price()
        print('Current Bitcoin Price: $' + str(price))

        # Send an emergency notification
        if price < self.THRESHOLD_AMOUNT:
            self.post_ifttt_webhook('bitcoin_price_emergency', price)

        # Send a notification if bitcoin price is higher then threshold
        else:
            self.post_ifttt_webhook('current_bitcoin_price', price)

        # Send a Telegram notification
        # Once we have 5 items in our bitcoin_history send an update
        for _ in range(1, 6):
            date = datetime.now()
            bitcoinHistory.append({'date': date, 'price': price})
            if len(bitcoinHistory) == 5:
                self.post_ifttt_webhook('bitcoin_price_update', self.bitcoin_history(bitcoinHistory))
                bitcoinHistory = []


if __name__ == "__main__":

    bitcoin = bitcoinPriceNotification()
    bitcoin.main()
