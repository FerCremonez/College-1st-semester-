#limita o tamanho da lista
L=[0]*10
print(L)
for i in range(10):
    L[i]=int(input('Insira um valor:'))
    print(L)
print(L)

#cria a lista conforme o usuário digita
'''L=[]
for i in range (10): #tamanho da lista
   valor=int(input('{}º valor -->'.format(i+1)))
   L.append(valor)
   print(L)
print(L)'''

from random import randint
L=[]
for i in range(5):
    