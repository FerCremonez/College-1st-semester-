for cont in range(1,51):
    med=float(input('Digite a média final:'))
    if cont==1:
        maior=med
        menor=med
    else:
        if med > maior:
            maior = med
        else:
            if med<menor:
                menor=med
print('Maior nota: ',maior)
print('Menor nota: ', menor)