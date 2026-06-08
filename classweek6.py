import pandas as pd
df = pd.read_csv("world_development_data.csv")
print(df)

print(df.head())
print(df.describe())
print(df.shape)
print(df.info())
