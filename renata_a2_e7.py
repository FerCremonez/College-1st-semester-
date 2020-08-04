preco=float(input('Preço do combustível em R$: '))
desempenho=int(input('Desempenho de veículo em Km/L: '))
dist=int(input('Distância do trajeto em Km:'))
litrogasto=dist/desempenho
moneygasto=preco*litrogasto
print('A quantidade de litros gastos no percurso é: {:.2f}'.format(litrogasto))
print('O dinheiro gasto foi de R$ {:.2f}'.format(moneygasto))