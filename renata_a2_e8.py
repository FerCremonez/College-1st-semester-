qtekm=int(input('Km percorridos:'))
qtedias=int(input('Dias alugados:'))
calc1=qtedias*60
calc2=qtekm*0.15
calcf=calc1+calc2
print('O total a ser pago é R$ {:.2f}'.format(calcf))