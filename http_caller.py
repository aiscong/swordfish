import urllib.request
import json


class HttpCaller:
    def get(self, url):
        response = urllib.request.urlopen(url)
        return json.load(response)

    def get_historical_quotes_url(self, stock, interval, span, bounds):
        url = 'https://api.robinhood.com/quotes/historicals/' + stock.upper() + \
              '/?&interval=' + interval.lower() + '&span=' + span.lower() + \
              '&bounds=' + bounds.lower()
        return url
