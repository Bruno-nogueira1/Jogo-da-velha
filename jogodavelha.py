import random
import copy
from tkinter import N

main = True
vitoria = False
dif = sentido = coluna = 0

tabuleiro = [['-' for c in range(3)]for x in range(3)]


#Muda a cor do texto de vitória
def vitoria_verde(texto):
    print('\033[1;32m'+texto+'\033[m')


#Mostra o tabuleiro atual
def mostrar_tabuleiro(tabuleiro, linhas):
    v = 0
    for c in tabuleiro:
        print(' -------------'+'-'*linhas)
        for x in c:
            if v == 0:
                print(' | '+ str(x), end=' | ')
                v += 1
            else:
                print(x, end=' | ')
        print('\n -------------'+'-'*linhas)
        v = 0


#Define a posição que o jogador irá escolher
def jogador():
    linha = 0
    coluna = 0
    escolha = True
    while escolha:
        while not 0 < linha < 4:
            linha = int(input('''Insira a linha: 
[1]
[2]
[3]
'''))
            if not 0 < linha < 4:
                print('\033[1;31mInsira uma linha existente\033[m')
        while not 0 < coluna < 4:
            coluna = int(input('''Insira a coluna: 
[1]     [2]     [3]
'''))
            if not 0 < coluna < 4:
                print('\033[1;31mInsira uma coluna existente\033[m')
        if tabuleiro[linha-1][coluna-1] == '-':
            tabuleiro[linha-1][coluna-1] = 'O'
            escolha = False
        else:
            print('\033[1;31mPosição ocupada\033[m')
            linha = 0
            coluna = 0


#Define a forma que o Computador irá jogar de acordo com a dificuldade
def dificuldade(x,sentido,coluna):
    #Irá escolher as posições aleatoriamente
    if x == 1:
        ok = True
        while ok:
            n = random.randint(0,2)
            n1 = random.randint(0,2)
            if tabuleiro[n][n1] == '-':
                tabuleiro[n][n1] = 'X'
                ok = False
    #Irá preencher o tabuleiro em uma coluna horizontal ou vertical, e caso não seja possível irá preencher aleatoriamente
    if x == 2:
        ok = False
        #Horizontal
        if sentido == 1:
            for c in range(0,2):
                if tabuleiro[coluna][c] == '-':
                    ok = True
            if ok:        
                while ok:
                    n = random.randint(0,2)
                    if tabuleiro[coluna][n] == '-':
                        tabuleiro[coluna][n] = 'X'
                        ok = False
            else:
                while not ok:
                    n = random.randint(0,2)
                    n1 = random.randint(0,2)
                    if tabuleiro[n][n1] == '-':
                        tabuleiro[n][n1] = 'X'
                        ok = True
        #Vertical
        if sentido == 2:
            for c in range(0,2):
                if tabuleiro[c][coluna] == '-':
                    ok = True
            if ok:
                while ok:
                    n = random.randint(0,2)
                    if tabuleiro[n][coluna] == '-':
                        tabuleiro[n][coluna] = 'X'
                        ok = False
            else:
                while not ok:
                    n = random.randint(0,2)
                    n1 = random.randint(0,2)
                    if tabuleiro[n][n1] == '-':
                        tabuleiro[n][n1] = 'X'
                        ok = True
    #Irá preencher ao redor das marcações do adversário
    if x == 3:
        ok = True
        v = 0
        tabuleiro_dif_3 = copy.deepcopy(tabuleiro)
        for c in tabuleiro_dif_3:
            for x in c:
                if x == 'O':
                    coluna = c.index(x)
                    linha = tabuleiro_dif_3.index(c)
                    tabuleiro_dif_3[linha][coluna] = '/'
        while ok:
            if linha == 0:
                n = random.choice([0,1])
            if linha == 1:
                n = random.choice([-1,0,1])
            if linha == 2:
                n = random.choice([0,-1])
            if coluna == 0:
                if n == 0:
                    n1 = 1
                else:
                    n1 = random.choice([0,1])
            if coluna == 1:
                if n == 0:
                    n1 = random.choice([-1,1])
                else:
                    n1 = random.choice([-1,0,1])
            if coluna == 2:
                if n == 0:
                    n1 = -1
                else:
                    n1 = random.choice([0,-1])
            if tabuleiro[linha+n][coluna+n1] == '-':
                tabuleiro[linha+n][coluna+n1] = 'X'
                ok = False
            v += 1
            if v == 4:
                while ok:
                    n = random.randint(0,2)
                    n1 = random.randint(0,2)
                    if tabuleiro[n][n1] == '-':
                        tabuleiro[n][n1] = 'X'
                        ok = False


#Verifica se houve um vencedor
def verifica_vitoria():
    global vitoria
    for c in range(0,3):
        #Horizontal
        if tabuleiro[c][0] == tabuleiro[c][1] == tabuleiro[c][2] == 'O':
            vitoria_verde('Vitória do Jogador')
            vitoria = True
        if tabuleiro[c][0] == tabuleiro[c][1] == tabuleiro[c][2] == 'X':
            vitoria_verde('Vitória do Computador')
            vitoria = True
        #Vertical
        if tabuleiro[0][c] == tabuleiro[1][c] == tabuleiro[2][c] == 'O':
            vitoria_verde('Vitória do Jogador')
            vitoria = True
        if tabuleiro[0][c] == tabuleiro[1][c] == tabuleiro[2][c] == 'X':
            vitoria_verde('Vitória do Computador')
            vitoria = True
    #Diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] =='O':
        vitoria_verde('Vitória do Jogador')
        vitoria = True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] =='X':
        vitoria_verde('Vitória do Computador')
        vitoria = True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == 'O':
        vitoria_verde('Vitória do Jogador')
        vitoria = True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == 'X':
        vitoria_verde('Vitória do Computador')
        vitoria = True


#O jogador escolhe a dificuldade do jogo
def escolher_dificuldade():
    global dif
    while not 0 < dif < 4 :
        dif = int(input('''Escolha uma dificuldade 
\033[32m[1] Fácil\033[m
\033[36m[2] Normal\033[m
\033[31m[3] Difícil\033[m
'''))
    if dif == 2:
        global sentido
        global coluna
        sentido = random.choice([1,2])
        coluna = random.randint(0,2)

#Verifica se houve empate
def empate():
    global vitoria
    n = 0
    for c in tabuleiro:
        for x in c:
            if x == '-':
                n += 1
    if n == 0:
        print('\033[1;30mO jogo terminou em Empate\033[m')
        vitoria = True

#Irá mostrar o menu ao jogador
def menu_def():
    global menu
    print('-'*14)
    print('\033[1mJogo da Velha \033[m')
    print('-'*14)
    menu = int(input('''\033[1m-----MENU-----
[1] Jogar      
[2] Instruções 
[3] Sair       
--------------
\033[m'''))
    while not 0 < menu < 4:
            menu = int(input('''-----MENU-----
[1] Jogar      
[2] Instruções 
[3] Sair       
--------------
'''))

#Programa principal
while main:
    menu_def()
    if menu == 1:
        while menu == 1:
            escolher_dificuldade()
            while not vitoria:
                jogador()
                mostrar_tabuleiro(tabuleiro,0)
                verifica_vitoria()
                print('===============')
                if not vitoria:
                    empate()
                    if not vitoria:
                        dificuldade(dif,sentido,coluna)
                        mostrar_tabuleiro(tabuleiro,0)
                        verifica_vitoria()
                        print('''\033[33m--------------
Próxima rodada
--------------\033[m''')
            if vitoria:
                rep = input(('Deseja continuar jogando? [S/N] '))
                while not rep in 'SsNn':
                    rep = input(('Deseja continuar jogando? [S/N]'))
                if rep in 'sS':
                    dif = 0
                    menu = 0
                    vitoria = False
                    tabuleiro = [['-' for c in range(3)]for x in range(3)]
                else:
                    break
    if menu == 2:      
        tabuleiro_instrucao = [['1,1','1,2','1,3'],['2,1','2,2','2,3'],['3,1','3,2','3,3']]
        print('''\033[1;35mO jogador utilizará o X enquanto o Computador o O
Irá sair vitorioso o primeiro a ter concluído o tabuleiro de forma horizontal, vertical ou diagonal
O tabuleiro irá seguir o seguinte padrão \033[m''')
        mostrar_tabuleiro(tabuleiro_instrucao,6)
    if menu == 3:
        break