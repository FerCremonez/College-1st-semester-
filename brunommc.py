List1 = []
List2 = []
List3 = []
n1 = int(input('Insira o primeiro dos MMCs: '))
n2 = int(input('Insura o segundo dos MMCs: '))
cond1 = True
cond2 = True
i = 1
h = 1
if n1 > n2:
    n3 = n1 ** 2
elif n2 > n1:
    n3 = n2 ** 2
while cond1:
     List1.append(n1 * i)
     if (n1 * i) > n3:
         break
     i += 1
while cond2:
     List2.append(n2 * h)
     if (n2 * h) > n3:
         cond2= False
         break
     h += 1
for j in List1:
    if j in List2:
        if not j in List3:
            List3.append(j)
print('Resultado:',List3[0])