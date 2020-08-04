print('informe as coordenadas de um ponto:')
x=int(input('x='))
y=int(input('y='))
if x==0 and y==0:
    print('origem')
elif x==0:
    print('eixo y')
elif y==0:
    print('eixo x')
elif x>0 and y>0:
    print('quadrante 1')
elif x<0 and y>0:
    print('quadrante 2')
elif x<0 and y<0:
    print('quadrante 3')
else:
    print('quadrante 4')
