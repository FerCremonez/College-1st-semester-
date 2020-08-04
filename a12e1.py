#exercício 1
a=[0]*5
for i in range(5):
    a[i]=[0]*5
    for j in range(5):
        a[i][j]=int(input())
print('Matriz:')
for i in range (5):
    print(a[i], "\n")
print('Diagonal secundária:')
for i in range(5):
    print(a[i][4-i])