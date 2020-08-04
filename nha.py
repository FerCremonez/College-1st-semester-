from random import randint

A = []
M = 0
m = 0
for i in range(10):
    A.append([])
    for j in range(10):
        A[i].append(randint(1, 99))
        print(f'[{A[i][j]:2}]', end=" ")
    print()
print('-' * 50)
for i in range(len(A)):
    for j in range(len(A)):
        if A[i][j] > M:
            M = A[i]
    print(M, i)
for i in range(len(A)):
    for j in range(len(A)):
        if A[i][j] < m:
            m = A[i]
    print(m, i)