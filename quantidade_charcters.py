senhaUsuario = input('Digite sua senha: ')
qtd_caracteres = len(senhaUsuario)


print(f'{senhaUsuario} -> possui {qtd_caracteres} letras')

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 8 caracters')

else:
    print('Você foi cadastrado com sucesso no sistema')
 