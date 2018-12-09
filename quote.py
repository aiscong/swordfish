
from http_caller import *
from data_point import *

def historical_quote(symbols, time_span, bound):

    caller = HttpCaller()

    historical_data_freq_combination = {'1d5min': ['5minute', 'day'],
                                        '1d10min': ['10minute', 'day'],
                                        '1w5min': ['5minute', 'week'],
                                        '1w10min': ['10minute', 'week'],
                                        '1y1d': ['day', 'year'],
                                        '5y1w': ['week', '']}
    hirtorical_data_bounds = ['extended', 'regular']

    symbols_list = ','.join(symbols).upper()
    interval = historical_data_freq_combination[time_span][0]
    span = historical_data_freq_combination[time_span][1]

    url = 'https://api.robinhood.com/quotes/historicals/?symbols=' + symbols_list + \
          '&interval=' + interval + '&span=' + span + '&bounds=' + bound.lower()

    quote_json = caller.get(url)

    quote = HistoricalPoint(quote_json)



    def pull_historical_data(stock, period, bounds):
        caller = HttpCaller()
        historical_url = caller.get_historical_quotes_url(stock, period[0], period[1], bounds)
        print(historical_url)
        quote_json = caller.get(historical_url)
        print(quote_json)
