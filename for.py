'''
for in em Python

Iterando strings com for

Função range (start = 0, stop, step=1)

            start = início
            stop = limite
            step = pulando de quanto em quanto
'''

texto = 'Python'
nova_string = ''

for numero in range(10):
    print(numero)

print('-=-' * 20)

texto1 = 'Estou estudando Python'

for letra in texto1:
    print(letra)

print('-=-' * 20)

for letra in texto1:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()

    else:
        nova_string += letra


print(nova_string)