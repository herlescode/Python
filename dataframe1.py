import pandas as pd

aluno = {
    'nome':['Ana', 'João', 'Maria', 'Luizinho'],
    'notap1':[8.5, 7.0, 9.5, 6.0],
    'notap2':[9.0, 6.5, 8.5, 7.5]
}
df_notas_aluno = pd.DataFrame(aluno)

print(df_notas_aluno)