nome = input('Qual é o seu nome? ')

if nome:
    print(nome)

else:
    print('Você não digitou nada =(')



print('-=-' * 20)
print('AGORA USANDO O OR')
print('-=-' * 20)

print(nome or 'Você não digitou nada!')
