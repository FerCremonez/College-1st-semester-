'''a=1
condicao=True
while a<=10:
    a+=1
    print(a)'''

'''nota=0
condicao=True
while condicao:
    nota=float(input('Digite a nota:'))
    if nota<0 or nota>10:
        print('Nota inválida')
    else:
        print('Nota', nota)
    condicao=nota<0 or nota>10'''

'''cont=0     #conta quantas pessoas
soma=0     #soma das idades
condicao=True
while condicao:
    idade=int(input('Digite a idade:'))
    if idade>0:
        cont+=1
        soma+=idade
    condicao=idade>0   #Encerra o bloco while

#sai do while (nova condição)
if  cont==0:
    print('Não houveram idades digitadas')
else:
    media=soma/cont
    print("média igual a:", media)'''


num=int(input('Digite um valor inteiro: '))
algarismos=0     #quantos algarismos tem o número
condicao=True
while condicao:
    num//=10
    algarismos+=1
    cond=num>0      #Encerra o bloco while

print('Total de algarismos:', algarismos)

'''#outra forma de fazer:
import math
num=int(input('Digite o numero: '))
print(int(math.log10(x))+1)'''