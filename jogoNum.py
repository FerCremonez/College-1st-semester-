#computador escolhe um númeero
from random import randint
numero = randint(1, 100)

correto=False       #começa com falso até o user acertar
tentativas=0        #adiciona o número de tentativas

while not correto:
    user=int(input('Qual número você acha que é?'))
    tentativas+=1
    if user==numero:
        correto=True
    else:
        #dicas
        if user<numero:
            print('Maior')
        elif user>numero:
            print('Menor')

#Quando o usuário acertar
print('PARABÉNS!')
print('Palpite correto após', tentativas, 'tentativas')
