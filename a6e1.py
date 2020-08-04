soma=0
cont=1
aprovados=0
reprovados=0
while (cont<=3):
    nota1=float(input('Primeira nota:'))
    nota2=float(input('Segunda nota:'))
    media=(nota1+nota2)/2

    soma+=media

    if media>=7:
        print('Aluno aprovado com média', media)
        aprovados+=1
    else:
        print('Aluno reprovado com média', media)
        reprovados+=1

media_geral=soma/3
print('Aprovados=', aprovados)
print('Reprovados=', reprovados)
print('Média geral da classe=', media_geral)
