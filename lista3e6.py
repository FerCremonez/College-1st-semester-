import math
print('informe os coeficientes de uma equação de 2º grau:')
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a==0:
    print('não é uma equação de 2º grau ')
else:
    delta=b**2 -4*a*c
    if delta<0:
        print('Não existe raiz real')
    else:
        if delta==0:
            x=(-b)/2*a
            print('raiz= {}. raiz unica')
        else:
            x1= (-b+math.sqrt(delta))/(2*a)
            x2= (-b-math.sqrt(delta))/(2*a)
            print('raízes x1={} e x2={}'.format(x1,x2))
