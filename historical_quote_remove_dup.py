
import glob
import pandas as pd


file_list = glob.glob("/Users/j0y01rf/PycharmProjects/swordfish/historical_data/*.csv")

for file in file_list:
    print(file)
    df = pd.read_csv(file)
    df = df.drop_duplicates()
    df.to_csv(file, index=False)