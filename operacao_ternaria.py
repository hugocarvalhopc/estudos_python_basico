

'''if logged_user == True:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa logar'

print(msg)
'''

print('-=-' * 20)
print('OPERAÇÃO TERNÁRIA')
print('-=-' * 20)

logged_user = False
msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar'

idade = 18

'''if idade > 18:
    print('Pode acessar!')

else:
    print('Não pode acessar')'''


msg1 = 'Pode acessar!' if idade > 18 else 'Não pode acessar'

print(msg1)


idade_user = input('Qual é a sua idade? ')

if not idade_user.isnumeric():
    print('Você precisa digitar apenas números')

else:
    idade_user = int(idade_user)
    e_de_maior = (idade_user >= 18)
    msg3 = 'Pode acessar' if e_de_maior else 'Não pode acessar.'


print(msg3)