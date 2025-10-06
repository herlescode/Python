import pandas as pd
import numpy as np

dados = {'Vendedor': ['João', 'Maria', 'Pedro', 'Ana'],
         'Vendas': [1000, 4000, np.nan, 2000],
         'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', np.nan]}

df_sem_nan = {'Vendedor': ['João', 'Maria', 'Pedro', 'Ana'],
         'Vendas': [1000, 4000, np.nan, 2000],
         'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', np.nan]}

df_vendas = pd.DataFrame(dados)
df_vendas_nan = pd.DataFrame(df_sem_nan)
df_vendas_preen = df_vendas_nan.dropna()
#df_vendas_preen = df_vendas_nan.fillna('#---#')
valor_branco = df_vendas.isnull().sum()
print("DataFrame original:")
print(df_vendas)
print(valor_branco)
print(df_vendas_nan)
print(df_vendas_preen)