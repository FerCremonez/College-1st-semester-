n,n2 = input("Insira um numero binario inteiro - >").split(",")
bins = list(map(int,n))
bins2 = list(map(int,n2))
x = len(bins)- 1
y = len(bins2) - 1
cont4 = y + 1
soma = 0
soma2 = 0
cont = x
cont2 = len(bins)
cont3 = len(bins2)
while cont2 > 0:
    if bins[x] == 1:
        soma += (2 ** cont)
    elif bins[x] == 0:
        soma += 0
    cont -= 1
    x -= 1
    cont2 -= 1
while cont3 > 0:
    if bins2[y] == 1:
        soma2 += (2 ** -(cont4))
    elif bins2[y] == 0:
        soma += 0
    cont4 -= 1
    y -= 1
    cont3 -= 1
soma3 = soma + soma2
print("{},{} : binário".format(n,n2))
print("{} : decimal".format(soma3))