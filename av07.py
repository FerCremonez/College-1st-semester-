from random import randint
#contador
cont = 0
x = True

while x:
    #sorteia um número
    n = randint(100, 999)

    #separa as casas
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    if a != b and  b!= c and a != c:
        x = False
x = True
print('Número sorteado:',n)

while x:
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    cont += 1

    #arruma o número
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a

    #menor número posível com aqueles algarismos
    menor = (a * 100) + (b * 10) + c

    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    if a < b:
        a, b = b, a

    #maior número possível com aqueles algarismos
    maior = (a * 100) + (b * 10) + c

    #vê se o valor da subtração é igual a 495
    n = maior - menor
    if n == 495:
        x = False

print('Iterações:',cont)

