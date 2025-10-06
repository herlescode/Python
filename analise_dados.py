import pandas as pd
import io

# Os dados do arquivo em formato de texto
dados_csv = """Rank,Name,Platform,Year,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales
1,Wii Sports,Wii,2006,Sports,Nintendo,41.49,29.02,3.77,8.46,82.74
2,Super Mario Bros.,NES,1985,Platform,Nintendo,29.08,3.58,6.81,0.77,40.24
3,Mario Kart Wii,Wii,2008,Racing,Nintendo,15.85,12.88,3.79,3.31,35.82
4,Wii Play,Wii,2006,Misc,Nintendo,14.7,9.2,2.93,2.85,29.05
5,Pokemon Red/Pokemon Blue,GB,1996,Role-Playing,Nintendo,11.27,8.89,10.22,1.0,31.37
6,Tetris,GB,1989,Puzzle,Nintendo,23.2,2.26,4.22,0.58,30.26
7,New Super Mario Bros.,DS,2006,Platform,Nintendo,11.38,9.23,6.5,2.9,30.01
8,Wii Fit,Wii,2007,Sports,Nintendo,8.94,8.03,3.6,2.15,22.72
9,Wii Fit Plus,Wii,2009,Sports,Nintendo,9.09,8.59,2.53,1.79,22.0
10,Duck Hunt,NES,1984,Shooter,Nintendo,26.93,0.63,0.28,0.47,28.31
"""

# Usa a biblioteca `io` para simular a leitura de um arquivo
df = pd.read_csv(io.StringIO(dados_csv))

# Agora continue com as etapas do exercício:
# 1. Mostre as 10 primeiras linhas do DataFrame
print(df.head(10))

# 2. Use .info() para verificar os tipos de dados
print(df.info())

# 3. Selecione e imprima a coluna 'Name'
print("\nColuna 'Name':")
print(df['Name'])

# 4. Selecione e imprima as colunas 'Name' e 'Platform'
print("\nColunas 'Name' e 'Platform':")
print(df[['Name', 'Platform']])