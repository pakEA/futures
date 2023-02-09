"""Программа, считывающая текущую цену фьючерса в реальном времени"""

import os

from dotenv import load_dotenv
from binance.um_futures import UMFutures

load_dotenv()

API_KEY = str(os.getenv('API_KEY'))
SECRET_KEY = str(os.getenv('SECRET_KEY'))
PRE_SYMBOL = 'XRP/USDT'
SYMBOL = PRE_SYMBOL.replace('/', '')


def comparison(current, max):
    percent = abs((current / max) * 100 - 100)
    if percent >= 1:
        print(f'Текущая цена "{round(current, 4)}" упала на {round(percent, 4)}%'
              f' от максимальной "{round(max, 4)}" за последний час.')


def main():
    while True:
        client = UMFutures(key=API_KEY, secret=SECRET_KEY)
        current_price = client.mark_price(SYMBOL)['markPrice']
        hour_candle = client.klines(SYMBOL, '1h', limit=1)
        max_price = hour_candle[0][2]
        comparison(float(current_price), float(max_price))


if __name__ == '__main__':
    main()
