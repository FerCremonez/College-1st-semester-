genero=str(input("Digite o sexo [M] ou [F]:")).upper()[0]
if(genero not in 'FM'):
    print('Gênero inválido')
else:
    h=float(input('Insira sua altura:'))
if (genero=='F'):
    peso=(62.1*h)-44.7
    print(f'\nO peso ideal de acordo com sua altura é: {peso:.1f} kg')
else:
    peso=(72.7*h)-58
    print(f'\nO peso ideal de acordo com sua altura é: {peso:.1f} kg')