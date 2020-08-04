N = int(input('Quantidade de elementos: '))
A = []

print('Elementos desejados:')
for i in range(N):
    A.append(int(input()))

A.sort()

print(f'Vetor A: \n{A}')

V = int(input('Digite o valor a ser inserido no vetor: '))

if V > A[-1]:
    A.append(V)
elif V < A[0]:
    A.insert(0, V)
else:
    for i in range(len(A)):
        if A[i] > V:
            A.insert((i), V) 
            break

print(f' Novo vetor: \n{A}')
