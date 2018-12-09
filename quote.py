
from http_caller import *
from data_point import *

def current_quote(symbols):
    caller = HttpCaller()
    symbol_list = ','.join(symbols).upper()
    url = 'https://api.robinhood.com/quotes/?symbols=' + symbol_list
    quote_json = caller.get(url)
    result = {}
    for raw_json_point in quote_json['results']:
        current_point = CurrentPoint(raw_json_point)
        result[current_point.symbol] = current_point

    return result


def historical_quote(symbols, time_span, bound):

    caller = HttpCaller()

    historical_data_freq_combination = {'1d5min': ['5minute', 'day'],
                                        '1d10min': ['10minute', 'day'],
                                        '1w5min': ['5minute', 'week'],
                                        '1w10min': ['10minute', 'week'],
                                        '1y1d': ['day', 'year'],
                                        '5y1w': ['week', '']}
    # historical_data_bounds = ['extended', 'regular']

    symbols_list = ','.join(symbols).upper()
    interval = historical_data_freq_combination[time_span][0]
    span = historical_data_freq_combination[time_span][1]

    url = 'https://api.robinhood.com/quotes/historicals/?symbols=' + symbols_list + \
          '&interval=' + interval + '&span=' + span + '&bounds=' + bound.lower()

    quote_json = caller.get(url)
    result = {}

    for raw_json_point_list in quote_json:
        result_list = []
        for raw_json_point in raw_json_point_list['historicals']:
            historical_point = HistoricalPoint(raw_json_point)
            result_list.append(historical_point)
        result[raw_json_point_list['symbol']] = result_list

    return result
