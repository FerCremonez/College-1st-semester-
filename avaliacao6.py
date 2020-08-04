#entrada
num1=int(input('Primeiro número:'))
num2=int(input('Segundo número:'))

#variáveis de contador
cont=0
contnum1=0
contnum2=0

#compara primeira entrada
while cont<num1:
    cont+=1
    if num1%cont==0:
        contnum1+=cont
contnum1-=num1

cont=0

#compara segunda entrada
while cont<num2:
    cont+=1
    if num2%cont==0:
        contnum2+=cont
contnum2-=num2

#compara se são amigos ou não
if contnum1==num2 and contnum2==num1:
    print('São amigos')
else:
    print('Não são amigos')
