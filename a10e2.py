A=[0]*10    #lista A com 10 valores
for i in range(10):
    A[i]=int(input('Digite os valores de A:'))  #entrada digitada pelo usuário

#Cria lista B e coloca input nela
B=[0]*10
for i in range(10):
    B[i]=int(input('Digite os valores de B:'))

#variável que irá conter a soma dos elementos das listas A e B
C=[0]*10
for i in range(10):
    C[i]=A[i]+B[i]
print('Vetor resposta:',C)


