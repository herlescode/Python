import pandas as pd
import numpy as np

df_vendas = {'Carros': ['Toro', 'Corolla', 'Plaza', np.nan],
         'Vendas': [84000, 68000, 85000, 82000],
         'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', np.nan]}

ler_vendas = pd.DataFrame(df_vendas).isnull().sum()
#new_dataframe = pd.DataFrame(df_vendas).dropna()
df_preenchido = pd.DataFrame(df_vendas).fillna({'Carros': 'Sem Carro', 'Vendas': 0, 'Cidade': 'Sem cidade'})

print(ler_vendas)
print(df_preenchido)
