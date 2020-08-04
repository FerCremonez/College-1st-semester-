massa=float(input('Digite a massa do objeto:'))
mi=massa
tempo=0
while massa>=0.5:
    tempo+=50
    massa/=2     #divide pela metade

#tempo = 7850 #segundos
h= tempo//3600
m=tempo%3600//60
s=tempo%60

print('Massa inicial: ',mi)
print('Massa final:' ,massa)
print('Tempo:', h,'horas',m,'minutos',s,'segundos')
