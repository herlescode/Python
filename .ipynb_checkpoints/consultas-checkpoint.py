import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df =  pd.read_csv('dados_vendas.csv')

#print (df.head())
#print (df.info())
#print (df.describe())

vendas_por_regiao = df.groupby('Regiao')['Valor_Total'].sum().reset_index()
#print(vendas_por_regiao)

#produto_mais_vendido = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)
produto_mais_vendido = df.groupby('Produto')['Quantidade'].sum().reset_index().sort_values(by='Quantidade', ascending=True)
#print(produto_mais_vendido)

#df['valor_total_com_descontos'] = df['Quantidade'] * df['Preco_Unitario'] * (1 - df['Desconto'])
#print(df.head())

sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.barplot(x='Regiao', y='Valor_Total', data=vendas_por_regiao)
plt.title('Total de Vendas por Região')
plt.xlabel('Região')
plt.ylabel('Valor Total')
plt.show()

plt.figure(figsize=(8, 4))
# A coluna no seu DataFrame original é 'Produto' (com O), não 'Protuto' (com T)
sns.barplot(x='Produto', y='Quantidade', data=produto_mais_vendido) 
plt.title('Produto mais vendido')
plt.xlabel('Produto')
plt.ylabel('Quantidade')
plt.show()
