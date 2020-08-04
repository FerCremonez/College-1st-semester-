name='abc'
pswrd='1234'
cont=3

while cont>=1:
    login=str(input('Usuário: '))
    password=str(input('Senha: '))

    if name==login and pswrd==password:
        print('Login efetuado com sucesso!')
        break

    else:
        cont-=1
        print('Login INCORRETO!',cont, 'tentativas restantes.')