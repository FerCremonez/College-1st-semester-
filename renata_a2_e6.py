sal=float(input('Insira o salário em R$:'))
reaj=float(input('Insira a taxa de reajuste em %:'))
calc=sal*reaj
calc2=calc/100
salf=calc2+sal
print('Salário final:',salf)
