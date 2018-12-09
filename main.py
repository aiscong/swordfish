from http_caller import *
from data_point import *

def main():
    caller = HttpCaller()
    quote_json = caller.get("https://api.robinhood.com/quotes/MSFT/")
    quote = CurrentPoint(quote_json)
    print(quote_json)
    print(quote.previous_close_date)


main()