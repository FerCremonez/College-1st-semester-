dia=int(input('Quantidade de dias:'))
hora=int(input('Quantidade de horas:'))
min=int(input('Quantidade de minutos:'))
seg=int(input('Quantidade de segundos:'))
calcdia=dia*86400
calchora=hora*3600
calcmin=min*60
calcseg=seg*1
calctotal=calcdia+calchora+calcmin+calcseg
print('A soma dessa desgraça é',calctotal,'s')