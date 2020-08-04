#100g=3.20
peso=float(input('Insira o peso do prato em g:'))
desc = peso-50
calc=(desc*3.20)/100
print(f"O total a ser pago é R$ {calc:.2f}")