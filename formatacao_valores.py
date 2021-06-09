'''
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:. (Número) f - quantidade de casas decimais (float)
: (caractere) (> ou < ou ^) (quantidade) (tipo  -s, d ou f)


> - Esquerda
< - Direita
^ - Centro
'''


num_1 = 1

print(f'{num_1:0<10}')

nome = 'Hugo carvalho'
print(f'{nome:=^20}')

print('-=-' * 20)

print(nome.lower()) #tudo minusculo
print(nome.upper()) #tudo maiusculo
print(nome.title()) # primeiras letras maiusculas