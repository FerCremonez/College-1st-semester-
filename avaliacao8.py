N=[]
i = 0

#Quantos alunos tiraram a mesma nota
contador1 = 0
contador2 = 0

while i<20:
    x = float(input('Insira as notas: '))

    #Validação de 0 a 10
    if x > 10 or x < 0:
        print('Nota inválida! Digite novamente.')
    else:
        N.append(x)
        i += 1

#Deixa em ordem crescente
N.sort()

#Maior e menor nota
menor = N[0]
maior = N[-1]

for i in N:
    if i == menor:
        contador1 += 1
    elif i == maior:
        contador2 += 1

print(f'Menor nota = {menor} e foram {contador1} alunos que a tiraram.')
print(f'Maior nota = {maior} e foram {contador2} alunos que a tiraram.')

