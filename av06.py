umaquinze = 1   #conta de 1 a 15
teste = 1       #valor a ser testado
cont = 0        #contador
x = True
while x:
    while umaquinze <= 15:
        if teste % umaquinze == 0:
            cont += 1
            umaquinze += 1
        else:
            teste += 1
            umaquinze = 1
            cont = 0
    if cont == 15:
        x = False

    print('O menor número divisível de 1 a 15 é: ',teste) #360360


