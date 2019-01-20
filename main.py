from quote import *
from instrument import *
from trader import *
import time, threading
import sys
import csv
from http_caller import *

def main():
    #
    # print(current_quote(['TQQQ','QQQ', 'TVIX', 'SPY' ]))
    # threading.Timer(3, main).start()
    #
    # print(historical_quote(['TQQQ', 'TVIX'], '1d5min', 'regular'))

    # print(get_instrument('MSFT'))
    # print(get_instruments(['TQQQ', 'TVIX', 'SPY', 'QQQ']))
    auth = open('safe', 'r').readline().split(':')
    trader = Trader(auth[0], auth[1])
    print(historical_quote(trader, ['TQQQ', 'TVIX'], '1d5min', 'regular'))


    # caller = HttpCaller()
    # popular = caller.get('https://api.robinhood.com/midlands/tags/tag/100-most-popular/')['instruments']
    #
    # # print(watch_list)
    # symbols = set()
    # for pop in popular:
    #     symbols.add(get_instrument_by_id_url(pop).symbol)
    # for watch in watch_list['results']:
    #     symbols.add(get_instrument_by_id_url(watch['instrument']).symbol)
    #
    # for p in position['results']:
    #     symbols.add(get_instrument_by_id_url(p['instrument']).symbol)
    #
    # print(symbols)
    #
    # with open("output.csv", 'w') as resultFile:
    #     wr = csv.writer(resultFile)
    #     wr.writerow(list(symbols))
    #
    # while (True):
    #     line = input("> ")
    #     print(line)

main()