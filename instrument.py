from http_caller import *
from data_point import *


def get_instruments(symbols):
    result = {}
    for symbol in symbols:
        result[symbol] = get_instrument(symbol)

    return result


def get_instrument(symbol):
    params = {'symbol': str(symbol).upper()}
    url = 'https://api.robinhood.com/instruments/'
    caller = HttpCaller()
    return Instrument(caller.get(url, params)['results'][0])

