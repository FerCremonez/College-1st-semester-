nota_trabalho = float(input("Informe a nota do trabalho de laboratório-> "))
if nota_trabalho<0 or nota_trabalho>10:
    print("Nota do trabalho inválida!!")
else:
    nota_avaliacao = float(input("Informe a nota da avaliação-> "))
    if nota_avaliacao<0 or nota_avaliacao>10:
        print("Nota da avaliação inválida")
    else:
        nota_exame = float(input("Informe a nota do exame-> "))
        if nota_exame<0 or nota_exame>10:
            print("Nota do exame inválida")
        else:
            media = (nota_trabalho*2+nota_avaliacao*3+nota_exame*5)/10
            if 0<=media<3:
                print("Aluno reprovado com média = {:.2f}".format(media))
            elif 3<=media<5:
                print("Aluno ficou de recuperação com média = {:.2f}".format(media))
            else:
                print("Aluno aprovado com média = {:.2f}".format(media))