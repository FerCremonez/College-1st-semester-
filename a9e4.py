num=int(input('Digite um número:'))
inv=0
while num>0:
    inv=inv*10+num%10
    num//=10
print('Número invertido:',inv)