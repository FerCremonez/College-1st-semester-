num=bool(input('Insira um número'))
bin=True
while num!=0:
    d=num%10
    num //= 10
    print(d)
    if d!=1 and d!=0:
        bin=False
        break
if bin==True:
    print('É binário')
else:
    print('Não é binário')
