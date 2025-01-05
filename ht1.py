import pandas as pd

df = pd.read_csv('Student Depression Dataset.csv')

print(df.head())
print(df.info())
print(df.describe())