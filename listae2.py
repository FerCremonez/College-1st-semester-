#Faça um programa em Python que gere 20 números aleatórios (entre 1 e 50), imprima
#os números e calcule a média apenas dos números pares.

from random import randint
lista=[]
for i in range (20):
    lista.append(randint(1,50))
print(lista)

cont=0
media=0
for n in lista:
    if n%2==0:
        media+=n
        cont+=1
media/=cont
print('Média dos números pares:',media)

