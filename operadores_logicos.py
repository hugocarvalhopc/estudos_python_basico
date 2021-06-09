'''
Operadores Lógicos

and = e, or = ou, not = negação

in e not in

'''


nome = 'Hugo Carvalho'

if 'a' in nome:
    print('Existe!')

if 'd' not in nome:
    print('Não existe!')


print('-=-' * 20)
print('{:^60}'.format('LOGIN'))
print('-=-' * 20)

usuario = input('Nome do Usuário: ')
senha = input('Senha do Usuário: ')

usuario_bd = 'hugo'
senha_bd = '1234567'

if usuario_bd == usuario and senha_bd == senha:
    print('logado com sucesso!')

else:
    print('Acesso NEGADO!')