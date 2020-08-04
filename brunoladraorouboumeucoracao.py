'''#ceiling  (pull up)
n=float(input('Insira o número:'))
n+=1
n=int(n)
print(n)'''

'''# floor (pull down)
n=float(input('Insira o número:'))
n-=1
n=int(n)
print(n)'''

'''#int (truncamento)
n = float(input('Insira o número:'))
print(int(n))'''

#Significa “qual o resto inteiro da divisão de k por M.
#Se k> 0, é só dividir k por M e pegar o resto.
#Se k<0, divida |k| por M para obter o resto a.
#Então faça, k(mod M) = M – a.

#função resto
'''m=float(input('Valor de m (menor que k e maior que 0):'))
k=float(input('Valor de k (inteiro):'))
if k>0:
    x=k%m
    print(x)
else:
    a=k%m
    y=m-a
    print(y)'''

#Crie um programa para executar a função Resto para k > 0, outro para
#k<0, e outro para qualquer valor de k.
k = int(input('m:'))
m = int(input('k:'))
if k > 0:
    result = k % m
if k < 0:
    result2 = (k * -1) % m
    result = m - result2
print(result)

