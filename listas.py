'''
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, min, max, range
'''

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)

l2.append('B')

l2.insert(1, 'Banana')

l2.pop()

del(l2[3:5])

print(l1)
print(l2)

print('-=-' * 20)
print('Outros testes')
print('-=-' * 20)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(max(numeros))
print(min(numeros))

print('-=-' * 20)
print('Outros testes')
print('-=-' * 20)

l3 = list(range(1, 21))
print(l3)

print('-=-' * 20)
print('Outros testes')
print('-=-' * 20)

l4 = ['String', True, 10, -20.5]

for elem in l4:
    print(f'O tipo de elemento é {type(elem)} e seu valor é {elem}')


print('-=-' * 20)
print('Outros testes')
print('-=-' * 20)

secreto = 'perfume'
digitadas = []
chances = 3

while True:

    if chances <= 0:
        print('Você perdeu :(')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHULLLL, a letra "{letra}" EXISTE na palavra secreta')

    else:
        print(f'AFFFzzz, a letra "{letra}" NÃO EXISTE na palavra secreta')
        digitadas.pop()

        secreto_temporario = ''
        for letra_secreta in secreto:
            if letra_secreta in digitadas:
                secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

        if secreto_temporario == secreto:
            print(f'Você GANHOU!!! A palavra secreta era {secreto_temporario}')
            break
        else:
            print(f'A palavra secreta está assim: {secreto_temporario}')

        if letra not in secreto:
            chances -= 1

        print(f'Você ainda tem {chances} chances.')
        print()