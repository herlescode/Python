import pandas as pd
df = pd.read_csv('dados_vendas.csv')

vendas_por_regiao = df.groupby('regiao')['valor_total'].sum().reset_index()
print(vendas_por_regiao)

vendas_por_vendedor = df.groupby('vendedor')['valor_total'].sum().reset_index()
print(vendas_por_vendedor)

produto_mais_vendido = df.groupby('produtor')['quantidade'].sum().sort_values(ascending=False)
print(produto_mais_vendido.head())

df['valor_total_com_desconto'] = df['quantidade'] * df['preco_unitario'] * (1 - df['desconto'])
print(df.head())