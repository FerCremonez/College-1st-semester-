cond = True
List = []
List2 = []
List3 = []
ListFinal = []
cont = 1
mdc = 0
while cond:
    N = input('Insira o número desejado e pressione x para encerrar:')
    if N != 'x':
        N = int(N)
    elif N == 'x':
        break
    cond = N != 'x'
    List2 = []
    for i in range(1,int(N)+1):
        if N % i == 0:
            if cont == 1:
                List.append(i)
            elif cont >1:
                List2.append(i)
                for z in List:
                  if z in List2:
                    if not z in List3:
                     List3.append(z)
            ListFinal = list(List3)
    if cont > 1:
       List = List3
       List3 = []
    cont += 1
mdc = ListFinal[0]
for i in ListFinal:
    if i > mdc:
        mdc = i
print('Resultado:',mdc)


#183177813