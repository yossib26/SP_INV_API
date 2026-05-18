import pandas as pd

df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

print(df.head())
print(df.shape)
print(df.columns.tolist())
