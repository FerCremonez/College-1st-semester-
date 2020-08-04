#estrutura para input de matriz

a=[0]*5     #define com 5 linhas
print('Digite os elemetos da matriz:')
for i in range(5):
    a[i]=[0]*5
    for j in range(5):
        a[i][j]=int(input())
print(a)

#para mostrar diagonal principal
print('Diagonal principal:')
for i in range(5):
    for j in range(5):
        if i==j:
            print(a[i][i])

#outro jeito mais curto de mostrar diagonal principal
#estrutura para input de matriz
a=[0]*5 #define com 5 linhas
print('Digite os elemetos da matriz:')
for i in range(5):
    a[i]=[0]*5
    for j in range(5):
        a[i][j]=int(input())

print('Diagonal principal:')
for i in range(5):
    print(a[i][i])
