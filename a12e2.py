#exercício 2
a=[0]*5
for i in range(5):
    a[i] = [0] * 5
    for j in range(5):
        a[i][j]=int(input())

print('Triangulo superior direito:')
for i in range(4):
    for j in range(i+1,5):
        print(a[i][j])
    print("\n")