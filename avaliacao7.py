#contadores
x=True
conta=0
contb=0
contc=0

while x:

    #entrada
    amigoa=int(input('Amigo A:'))
    amigob=int(input('Amigo B:'))
    amigoc=int(input('Amigo C:'))

#amigo A ganha a rodada
    if (amigoa==1 and amigob==2 and amigoc==2) or (amigoa==2 and amigob==1 and amigoc==1):
        conta += 1
        print('Amigo A venceu essa rodada ')


#Amigo B ganha a rodada
    elif (amigob==1 and amigoa==2 and amigoc==2) or (amigob==2 and amigoa==1 and amigoc==1):
        contb+=1
        print('Amigo B venceu essa rodada')

#amigo C ganha a rodada
    elif (amigoc==1 and amigoa==2 and amigob==2) or (amigoc==2 and amigoa==1 and amigob==1):
        contc+=1
        print('Amigo C venceu esa rodada')

    if conta == 3:
        print("Amigo A é o vencedor!!")

    if contb == 3:
        print('Amigo B é o vencedor!!')

    if contc == 3:
        print('Amigo C é o vencedor!!')
        x=False