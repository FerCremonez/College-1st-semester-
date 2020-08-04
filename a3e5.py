tempo=int(input('Insira o tempo:'))
hora=tempo//3600
min=hora%3600
min2=min//60
seg=tempo%10
print('hora:', hora)
print('min:', min2)
print('seg:', seg)


