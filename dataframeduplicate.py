import pandas as pd
import numpy as np


dados_duplicados = {'ID': [1, 2, 3, 1, 4, 3],
                    'Nome': ['Ana', 'João', 'Maria', 'Ana', 'Pedro', 'Maria']}

df_duplicado = pd.DataFrame(dados_duplicados)
retira_duplicates = df_duplicado.duplicated()
new_datafram = df_duplicado.drop_duplicates()
print("DataFrame original:")
print(retira_duplicates)
print("Removendo linhas duplicadas")
print(new_datafram)