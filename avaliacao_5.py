#entrada
condicao=True
num=100

while condicao:
    #separa em c,d,u
    c=num//100
    d=(num//10)%10
    u=num%10

    #verifica as condições
    if d>c and u>d:
        print('O número',num,'é ascendente')

    #conta+1
    num+=1

    #encerre o bloco while
    condicao=num<1000
