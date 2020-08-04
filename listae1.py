#Faça um programa em Python que gere 10 números aleatórios (entre 1 e 50), imprima
#os números e calcule quantos são números pares e quantos são números ímpares.

from random import randint
lista=[]
for i in range(10):   #quantidade de algarismos
    lista.append(randint(1,50))  #range entre os 10 algarismos
print(lista)

par=0
impar=0
for n in lista:
    if n%2==0:
        par+=1
    else:
        impar+=1
print('Existem {} números  pares e {} números ímpares'.format(par,impar))