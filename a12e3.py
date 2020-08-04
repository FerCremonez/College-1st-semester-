#exercício 3
a=[0]*5
for i in range(5):
    a[i] = [0] * 5
    for j in range(5):
        a[i][j]=int(input())

print('Triangulo inferior esquerdo:')
for i in range(1,5):
    for j in range(0,i):
        print(a[i][j],end='')
    print()