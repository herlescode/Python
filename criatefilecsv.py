import pandas as pd
import numpy as np

#cria um dicionario com dados de vendas
data = {
    'id_vendas': np.arange(101, 126),
    'data_venda': pd.to_datetime(pd.date_range(start='2024-01-01', periods=25, freq='D')),
    'produtor':['Notebook', 'Monitor', 'Mouse', 'Teclado', 'Cadeira Gamer'] * 5,
    'regiao': ['norte', 'sul', 'leste', 'oeste', 'leste'] * 5,
    'quantidade': np.random.randint(1, 20, size=25),
    'preco_unitario': np.random.uniform(50, 2000, size=25).round(2),
    'desconto': np.random.choice([0, 0.05, 0.1, 0.15], size=25),
    'vendedor': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'] * 5
}
#cria um dataframe a partir do dicionario
df = pd.DataFrame(data)

#calcula o valor total da venda aplicando o desconto
df['valor_total'] = (df['quantidade'] * df['preco_unitario']) * (1 - df['desconto'])

#salva o dataframe em um arquivo CSV
df.to_csv('dados_vendas.csv', index=False, encoding='utf-8')
          
#mensagem de sucesso
print("Arquivo CSV 'dados_vendas.csv' criado com sucesso!")