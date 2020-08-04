#valores de entrada
num1,num2,num3 = input("Insira 3 números: ").split()
A = (num1,num2,num3)
lt1,lt2,lt3,lt4 = input("Insira 4 letras: ").split()
B = (lt1,lt2,lt3,lt4)

#impressão dos conjuntos
print("{}".format(A))
print("{}".format(B))
print("A X B")

#contadores
cont1 = 0
cont2 = 0
cont3 = 0

#laço de repetição
for i in A:
    print("\n")
    for g in B:
      print("({},{})".format(i,g),end="")
      cont1 += 1
print("\n")
print("A X A")
for i in A:
    print("\n")
    for g in A:
        print("({},{})".format(i, g), end="")
        cont2 += 1
print('\n')
print("B X A")
for i in B:
    print("\n")
    for g in A:
        print("({},{})".format(i, g), end="")
        cont3 += 1
print("\n")
print("A X B = {}".format(cont1))
print('\n')
print("A X A = {}".format(cont2))
print('\n')
print("B X A = {}".format(cont3))