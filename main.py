from http_caller import *
from quote_point import *

def main():
    caller = HttpCaller()
    quote_json = caller.get("https://api.robinhood.com/quotes/MSFT/")
    quote = QuotePoint(quote_json)
    print(quote_json)
    print(quote.previous_close_date)


main()

historical_data_freq_combination = {'1day(5minute)': ['5minute', 'day'],
                                    '1day(10minute)': ['10minute', 'day'],
                                    '1week(5minute)': ['5minute', 'week'],
                                    '1week(10minute)': ['10minute', 'week'],
                                    '1year(day)': ['day', 'year'],
                                    '5year(week)': ['week', '']}
historical_data_type_option = ['extended', 'regular']
stock = 'GOOG'
bounds = 'regular'
period = historical_data_freq_combination['1day(5minute)']


def pull_historical_data(stock, period, bounds):
    caller = HttpCaller()
    historical_url = caller.get_historical_quotes_url(stock, period[0], period[1], bounds)
    print(historical_url)
    quote_json = caller.get(historical_url)
    print(quote_json)


pull_historical_data(stock, period, bounds)
