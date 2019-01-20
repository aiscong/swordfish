
from data_point import *


def current_quote(trader, symbols):
    symbol_list = ','.join(symbols).upper()
    params = {'symbols': symbol_list}
    url = 'https://api.robinhood.com/quotes/'
    quote_json = trader.http_get(url, params)
    result = {}
    for raw_json_point in quote_json['results']:
        current_point = CurrentPoint(raw_json_point)
        result[current_point.symbol] = current_point

    return result


def historical_quote(trader, symbols, time_span, bound):
    historical_data_freq_combination = {'1d5min': ['5minute', 'day'],
                                        '1d10min': ['10minute', 'day'],
                                        '1w5min': ['5minute', 'week'],
                                        '1w10min': ['10minute', 'week'],
                                        '1y1d': ['day', 'year'],
                                        '5y1w': ['week', '']}
    # historical_data_bounds = ['extended', 'regular']
    symbol_list = ','.join(symbols).upper()
    interval = historical_data_freq_combination[time_span][0]
    span = historical_data_freq_combination[time_span][1]
    params = {'symbols': symbol_list, 'interval': interval, 'span': span, 'bounds': bound.lower()}
    url = 'https://api.robinhood.com/quotes/historicals/'
    quote_json = trader.http_get(url, params)
    result = {}
    for raw_json_point_list in quote_json['results']:
        result_list = []
        for raw_json_point in raw_json_point_list['historicals']:
            historical_point = HistoricalPoint(raw_json_point)
            result_list.append(historical_point)
        result[raw_json_point_list['symbol']] = result_list

    return result
