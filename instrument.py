from http_caller import *
from data_point import *

def get_instrument(symbol):
    params = {'symbol': str(symbol).upper()}
    url = 'https://api.robinhood.com/instruments/'
    caller = HttpCaller()
    return Instrument(caller.get(url, params)['results'][0])

