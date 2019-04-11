from quote import *
from trader import *
import os
import pandas as pd
import numpy as np

symbols = pd.read_csv(os.getcwd() + '/stock_list.csv', header=None)
symbols = symbols.iloc[0, :].values
black_list = ['MULE', 'VXX', 'P', 'WIN']

symbols = np.setdiff1d(symbols, black_list)
time_span = '15min'
# time_span = '1d5min'
bound = 'regular'

auth = open('safe', 'r').readline().split(':')
trader = Trader(auth[0], auth[1])

for i in range((len(symbols) - 1) // 75 + 1):
    start_index = 75 * i
    end_index = min(75 * (i + 1), len(symbols))
    output = historical_quote(trader, symbols[start_index:end_index], time_span, bound)
    for symbol in symbols[start_index:end_index]:
        df = pd.DataFrame.from_records([i.to_dict() for i in output[symbol]])
        df = df[['timestamp', 'open', 'close', 'high', 'low', 'vol']]
        path = os.getcwd() + '/historical_data/' + symbol + '.csv'
        if os.path.exists(path):
            df.to_csv(path, mode='a', header=False, index=False)
        else:
            df.to_csv(path, header=True, index=False)

trader.log_out()
