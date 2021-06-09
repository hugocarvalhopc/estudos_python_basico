variavel = ['Luiz Otávio', 'Joãozinho', 'Maria']

for valor in variavel:
    if valor.lower().startswith('j'):
        continue
else:
    print('Não existe uma palavra com J.')