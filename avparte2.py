#Entrada
n=int(input('Insira n:'))

#Valores iniciais
matriz=[0]*n
nulo=0
valid=False
print('Digite os valores da Matriz:')

#Laços & verificações
for i in range(n):
    matriz[i]=[0]*n
    for j in range(n):
        matriz[i][j] = int(input('Valor:'))

for i in range(n):
    for j in range(n):
        print(f'{matriz[i][j]:2}', end=' ')
    print()

for i in range(n):
    for j in range(n):
        if matriz[j][i] != 0:
            valid = False
        else:
            valid = True
    if valid:
        nulo += 1
print(f'Há {nulo} colunas nulas na Matriz')