
from quote import *
import os
import pandas as pd

symbols = ['FB', 'GOOG']
time_span = '1w5min'
bound = 'regular'

output = historical_quote(symbols, time_span, bound)

for symbol in symbols:
    pwd = os.getcwd()
    path = pwd + '/historical_data/' + symbol + '.csv'

    df = pd.DataFrame.from_records([i.to_dict() for i in output[symbol]])
    df = df[['timestamp', 'open', 'close', 'high', 'low', 'vol']]

    if os.path.exists(path):
        df.to_csv(path, mode='a', header=False, index=False)
    else:
        df.to_csv(path, header=True, index=False)

