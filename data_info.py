import pandas as pd

df = pd.read_csv('healthcare-dataset-stroke-data.csv')

print(df)
print(df.info())
print(df.describe())

input()