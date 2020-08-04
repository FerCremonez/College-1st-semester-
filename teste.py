med1=float(input('Digite a 1ª nota:'))
med2=float(input('Digite a 2 nota:'))
calc=(med1+med2)/2

if calc >= 6:
    print('Aluno APROVADO com nota:',calc)
else:
    print('Aluno REPROVADO com nota:',calc)
