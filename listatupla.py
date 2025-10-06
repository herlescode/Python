catalogo = {
    'id_produto': 123,
    'nome': 'Mouse Óptico',
    'preço': 75.50,
    'disponivel': True
}

catalogo['especificacoes'] = ('cor', 'preto', 'peso', 0.150)

print(f"{catalogo['especificacoes'][3]}")

catalogo['preco'] = 80.0
catalogo['qnt em estoque'] = 250

print("\n", catalogo)