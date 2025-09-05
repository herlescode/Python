import pandas as pd

df = pd.read_csv('dados_vendas.csv')
print (df.head())
print(df.info())
print(df.describe())