import requests


# defining key/request url
def get_coin_price(coin_symbol):
    key = "https://api.binance.com/api/v3/ticker/price?symbol=" + coin_symbol + "USDT"
    # requesting data from url
    data = requests.get(key)
    data = data.json()
    # print(f"{data['symbol']} price is {data['price']}")
    return data['price']


get_coin_price("BTC")


def usd_coin_exchange(dollar_amount, coin_symbol):
    coin_amount = dollar_amount / float(get_coin_price(coin_symbol))
    return coin_amount


def coin_usd_exchange(coin_amount, coin_symbol):
    dollar_amount = float(get_coin_price(coin_symbol)) * coin_amount
    return dollar_amount
