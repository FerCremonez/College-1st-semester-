print(' * ' * 15)
print('                Jogo da Velha :) ')
print(' * ' * 15)

gameworking = True
vencedor = None

jatual = 'X'

tabuleiro = ['-', '-', '-', '-', '-', '-', '-', '-', '-']


def jogo():
    mostrar_tabuleiro()

    while gameworking:
        turno()

        game_parou()

        trocar_player()
    if vencedor == 'X' or vencedor == 'O':
        print(f'Parabéns, o vencedor é o {vencedor}')
    elif vencedor == None:
        print('Empate!')


def mostrar_tabuleiro():
    print('\n')
    print(f"       {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}      1 | 2 | 3")
    print(f"       {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}      4 | 5 | 6")
    print(f"       {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}      7 | 8 | 9")
    print()


def turno():
    print(f'É a vez do {jatual}!')
    posicao = input('Escolha uma posição de 1 a 9: ')

    valido = False
    while not valido:
        while posicao not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            posicao = input('Escolha uma posição de 1 a 9-> ')
        posicao = int(posicao) - 1
        if tabuleiro[posicao] != '-':
            print('Posição já ocupada! Escolha outra.')
        else:
            tabuleiro[posicao] = jatual
            valido = True
        mostrar_tabuleiro()


def game_parou():
    se_vencedor()
    se_empate()


def se_vencedor():
    global vencedor
    diagonal_vencedor = diagonais()
    linha_vencedor = linhas()
    coluna_vencedor = colunas()

    if diagonal_vencedor:
        vencedor = diagonal_vencedor
    elif linha_vencedor:
        vencedor = linha_vencedor
    elif coluna_vencedor:
        vencedor = coluna_vencedor


def se_empate():
    global gameworking
    if '-' not in tabuleiro:
        gameworking = False
        return True
    else:
        return False


def diagonais():
    global gameworking
    diagonal1 = tabuleiro[2] == tabuleiro[4] == tabuleiro[6] != '-'
    diagonal2 = tabuleiro[0] == tabuleiro[4] == tabuleiro[8] != '-'

    if diagonal1 or diagonal2:
        gameworking = False
    if diagonal1:
        return tabuleiro[0]
    elif diagonal2:
        return tabuleiro[2]
    else:
        return None


def linhas():
    global gameworking
    linha1 = tabuleiro[0] == tabuleiro[1] == tabuleiro[2] != '-'
    linha2 = tabuleiro[3] == tabuleiro[4] == tabuleiro[5] != '-'
    linha3 = tabuleiro[6] == tabuleiro[7] == tabuleiro[8] != '-'

    if linha1 or linha2 or linha3:
        gameworking = False
    if linha1:
        return tabuleiro[0]
    elif linha2:
        return tabuleiro[3]
    elif linha3:
        return tabuleiro[6]
    else:
        return None


def colunas():
    global gameworking
    coluna1 = tabuleiro[0] == tabuleiro[3] == tabuleiro[6] != '-'
    coluna2 = tabuleiro[1] == tabuleiro[4] == tabuleiro[7] != '-'
    coluna3 = tabuleiro[2] == tabuleiro[5] == tabuleiro[8] != '-'

    if coluna1 or coluna2 or coluna3:
        gameworking = False
    if coluna1:
        return tabuleiro[0]
    elif coluna2:
        return tabuleiro[1]
    elif coluna3:
        return tabuleiro[2]
    else:
        return None


def trocar_player():
    global jatual
    if jatual == "X":
        jatual = "O"
    elif jatual == "O":
        jatual = "X"


jogo()