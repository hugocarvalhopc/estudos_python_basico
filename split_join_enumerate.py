
print('-=-' * 20)
print('Testes com SPLIT')
print('-=-' * 20)


string = 'O Brasil é o país do futebol, o Brasil é penta'
lista_1 = string.split(' ')
lista_2 = string.split(',')

print(lista_1)
print(lista_2)


palavra = ''
contagem = 0

for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor


print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')


print('-=-' * 20)
print('Testes com JOIN')
print('-=-' * 20)

string_2 = 'O Brasil é penta.'
lista = string_2.split(' ')
string3 = ' '.join(lista)

print(string_2)
print(lista)
print(string3)

print('-=-' * 20)
print('Testes com ENUMERATE')
print('-=-' * 20)   

lista = ['Luiz', 'João', 'Maria']

for indice, nome in enumerate(lista):
    print(indice, nome)


print('-=-' * 20)
print('Testes com Desempacotamento')
print('-=-' * 20)

n1, n2, n3 = lista

print(n2)