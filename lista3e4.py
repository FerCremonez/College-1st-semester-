salario=float(input('Digite o salário:'))
valor=float(input('Valor da prestação:'))
parc=salario*0.2
if valor>parc:
    print('Emprestimo negado')
else:
    print('Empréstimo concedido')
