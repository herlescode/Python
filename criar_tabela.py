import pandas as pd
import numpy as np

# Cria um dicionário com os dados de exemplo
data = {
    'ID_Venda': np.arange(101, 126),
    'Data_Venda': pd.to_datetime(pd.date_range(start='2024-01-01', periods=25, freq='D')),
    'Produto': ['Notebook', 'Monitor', 'Mouse', 'Teclado', 'Cadeira Gamer'] * 5,
    'Regiao': ['Norte', 'Sul', 'Leste', 'Oeste', 'Leste'] * 5,
    'Quantidade': np.random.randint(1, 10, size=25),
    'Preco_Unitario': np.random.uniform(50, 2000, size=25).round(2),
    'Desconto': np.random.choice([0, 0.05, 0.1, 0.15], size=25),
    'Vendedor': ['Ana', 'Bruno', 'Carla', 'Daniela', 'Eduardo'] * 5
}

# Cria o DataFrame a partir do dicionário
df = pd.DataFrame(data)

# Calcula o Valor Total da Venda
df['Valor_Total'] = (df['Quantidade'] * df['Preco_Unitario']) * (1 - df['Desconto'])

# Salva o DataFrame em um arquivo CSV
# O index=False evita que o índice do DataFrame seja salvo como uma coluna
df.to_csv('dados_vendas.csv', index=False, encoding='utf-8')

print("Arquivo 'dados_vendas.csv' criado com sucesso!")