num1=int(input('Primeiro número:'))
num2=int(input('Segundo número:'))
cont=0
if num1>999 or num2>999:
    print('Digite um número de no máximo 3 algarismos')
else:
    #decompõe num1
    centena1=num1//100
    dezena1=num1%100//10
    unidade1=num1%10

    #decompoe num2
    centena2=num2//100
    dezena2=num2%100//10
    unidade2=num2%10

    if unidade1+unidade2>=10:
        cont+=1
        dezena1+=1

    if dezena1+dezena2>=10:
        cont += 1
        centena1+=1

    if centena1+centena2>=10:
        cont+=1

print(cont,'"vai 1"')



