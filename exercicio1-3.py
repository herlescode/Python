def make_sandwich(bread_type, filling, cheese='nenhum', toasted=False):
    if toasted:
        bread_type = f"{bread_type} torrado"
    
    texto = f"Preparar um sanduíche de {bread_type} com {filling}"
    
    if cheese != 'nenhum':
        texto += f" e queijo {cheese}"
    
    texto += "."
    
    return texto

print(make_sandwich("trigo", "peru", "cheddar", True))
print(make_sandwich("centeio", "presunto"))