a=int(input('Primeiro valor:'))
b=int(input('Segundo valor:'))
c=int(input('Terceiro valor:'))
if((a>b) and a>c):
    print('Maior valor = ', a)
elif (b>c):
    print('Maior valor =', b)
else:
    print('Maior valor = ', c)