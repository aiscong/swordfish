from quote import *
from instrument import *
import time, threading
import sys

def main():

    print(current_quote(['TQQQ', 'TVIX', 'SPY', 'QQQ']))
    threading.Timer(3, main).start()
    #
    # print(historical_quote(['TQQQ', 'TVIX'], '1d5min', 'regular'))

    # print(get_instrument('MSFT'))
    #
    #
    # while (True):
    #     line = input("> ")
    #     print(line)

main()