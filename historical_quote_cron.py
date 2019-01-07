
from quote import *
import os
import pandas as pd
import numpy as np

symbols = pd.read_csv('/Users/j0y01rf/PycharmProjects/swordfish/stock_list.csv', header=None)
symbols = symbols.iloc[0, :].values
black_list = ['MULE']

symbols = np.setdiff1d(symbols, black_list)
# time_span = '1w5min'
time_span = '1d5min'
bound = 'regular'

for i in range((len(symbols) - 1)/75 + 1):
    start_index = 75*i
    end_index = min(75*(i+1), len(symbols))
    output = historical_quote(symbols[start_index:end_index], time_span, bound)
    for symbol in symbols[start_index:end_index]:
        df = pd.DataFrame.from_records([i.to_dict() for i in output[symbol]])
        df = df[['timestamp', 'open', 'close', 'high', 'low', 'vol']]
        pwd = os.getcwd()
        path = pwd + '/historical_data/' + symbol + '.csv'
        if os.path.exists(path):
            df.to_csv(path, mode='a', header=False, index=False)
        else:
            df.to_csv(path, header=True, index=False)





