
# remove duplicates
# sort by timestamp

import glob
import pandas as pd
import os

file_list = glob.glob(os.getcwd() + "/historical_data/*.csv")

for file in file_list:
    print(file)
    df = pd.read_csv(file)
    df = df.drop_duplicates()
    df = df.sort_values('timestamp')
    df.to_csv(file, index=False)
