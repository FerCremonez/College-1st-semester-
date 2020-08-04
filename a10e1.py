lista=[7,15,4,8,9,20,5,2,12,10]
for i in range(10):
    maior=lista[0]
    menor=lista[0]

for i in range(1,10):
    if (lista[i]>maior):
        maior=lista[i]
    else:
        if lista[i] <menor:
            print('Maior:',maior, 'Menor:',menor)

