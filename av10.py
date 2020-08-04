a=[0]*5   #comprimento da linha
soma=0         #contador

#forma a lista
for i in range (5):
    a[i]=[0]*5
    for j in range(5):
        a[i][j]=int(input())

#printa linha
for i in a:
    print(i)

#soma das linhas
for i in range(5):
    for j in range(5):
        soma+=a[i][j]
    print(f'Soma da {i+1}ª linha = {soma}')
    soma=0

#pula 1 linha
print()

#somas das colunas
soma=0
for i in range(5):
    for j in range(5):
        soma+=a[j][i]
    print(f'Soma da {i+1}ª coluna = {soma}')
    soma=0




