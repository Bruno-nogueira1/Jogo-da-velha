import random
import copy

main = True
victory = False
dif = sense = column = 0

board = [['-' for c in range(3)]for x in range(3)]


#Change victory color to green
def victory_green(text):
    print('\033[1;32m'+text+'\033[m')


#Show the current board
def show_board(board, lines):
    v = 0
    for c in board:
        print(' -------------'+'-'*lines)
        for x in c:
            if v == 0:
                print(' | '+ str(x), end=' | ')
                v += 1
            else:
                print(x, end=' | ')
        print('\n -------------'+'-'*lines)
        v = 0


#Sets the position of the player's move
def player():
    line = 0
    column = 0
    choice = True
    while choice:
        while not 0 < line < 4:
            line = int(input('''Insira a linha: 
[1]
[2]
[3]
'''))
            if not 0 < line < 4:
                print('\033[1;31mInsira uma linha existente\033[m')
        while not 0 < column < 4:
            column = int(input('''Insira a coluna: 
[1]     [2]     [3]
'''))
            if not 0 < column < 4:
                print('\033[1;31mInsira uma coluna existente\033[m')
        if board[line-1][column-1] == '-':
            board[line-1][column-1] = 'O'
            choice = False
        else:
            print('\033[1;31mPosição ocupada\033[m')
            line = 0
            column = 0


#Sets the way the computer will play according to the difficulty
def difficulty(x, sense, column):
    #Sets the position randomly
    if x == 1:
        ok = True
        while ok:
            n = random.randint(0,2)
            n1 = random.randint(0,2)
            if board[n][n1] == '-':
                board[n][n1] = 'X'
                ok = False
    #It will fill the board in a horizontal or vertical column, and if not possible, it will fill randomly
    if x == 2:
        ok = False
        #Horizontal
        if sense == 1:
            for c in range(0,2):
                if board[column][c] == '-':
                    ok = True
            if ok:        
                while ok:
                    n = random.randint(0,2)
                    if board[column][n] == '-':
                        board[column][n] = 'X'
                        ok = False
            else:
                while not ok:
                    n = random.randint(0,2)
                    n1 = random.randint(0,2)
                    if board[n][n1] == '-':
                        board[n][n1] = 'X'
                        ok = True
        #Vertical
        if sense == 2:
            for c in range(0,2):
                if board[c][column] == '-':
                    ok = True
            if ok:
                while ok:
                    n = random.randint(0,2)
                    if board[n][column] == '-':
                        board[n][column] = 'X'
                        ok = False
            else:
                while not ok:
                    n = random.randint(0,2)
                    n1 = random.randint(0,2)
                    if board[n][n1] == '-':
                        board[n][n1] = 'X'
                        ok = True
    #Will fill around opponent's markings
    if x == 3:
        ok = True
        v = 0
        board_dif_3 = copy.deepcopy(board)
        for c in board_dif_3:
            for x in c:
                if x == 'O':
                    column = c.index(x)
                    line = board_dif_3.index(c)
                    board_dif_3[line][column] = '/'
        while ok:
            if line == 0:
                n = random.choice([0,1])
            if line == 1:
                n = random.choice([-1,0,1])
            if line == 2:
                n = random.choice([0,-1])
            if column == 0:
                if n == 0:
                    n1 = 1
                else:
                    n1 = random.choice([0,1])
            if column == 1:
                if n == 0:
                    n1 = random.choice([-1,1])
                else:
                    n1 = random.choice([-1,0,1])
            if column == 2:
                if n == 0:
                    n1 = -1
                else:
                    n1 = random.choice([0,-1])
            if board[line+n][column+n1] == '-':
                board[line+n][column+n1] = 'X'
                ok = False
            v += 1
            if v == 4:
                while ok:
                    n = random.randint(0,2)
                    n1 = random.randint(0,2)
                    if board[n][n1] == '-':
                        board[n][n1] = 'X'
                        ok = False


#Verifica se houve um vencedor
def check_victory():
    global victory
    for c in range(0,3):
        #Horizontal
        if board[c][0] == board[c][1] == board[c][2] == 'O':
            victory_green('Vitória do Jogador')
            victory = True
        if board[c][0] == board[c][1] == board[c][2] == 'X':
            victory_green('Vitória do Computador')
            victory = True
        #Vertical
        if board[0][c] == board[1][c] == board[2][c] == 'O':
            victory_green('Vitória do Jogador')
            victory = True
        if board[0][c] == board[1][c] == board[2][c] == 'X':
            victory_green('Vitória do Computador')
            victory = True
    #Diagonais
    if board[0][0] == board[1][1] == board[2][2] =='O':
        victory_green('Vitória do Jogador')
        victory = True
    if board[0][0] == board[1][1] == board[2][2] =='X':
        victory_green('Vitória do Computador')
        victory = True
    if board[0][2] == board[1][1] == board[2][0] == 'O':
        victory_green('Vitória do Jogador')
        victory = True
    if board[0][2] == board[1][1] == board[2][0] == 'X':
        victory_green('Vitória do Computador')
        victory = True


#Player sets the difficulty
def choose_difficulty():
    global dif
    while not 0 < dif < 4 :
        dif = int(input('''Escolha uma dificuldade 
\033[32m[1] Fácil\033[m
\033[36m[2] Normal\033[m
\033[31m[3] Difícil\033[m
'''))
    if dif == 2:
        global sense
        global column
        sense = random.choice([1,2])
        column = random.randint(0,2)


#Check if there is a tie
def tie():
    global victory
    n = 0
    for c in board:
        for x in c:
            if x == '-':
                n += 1
    if n == 0:
        print('\033[1;30mO jogo terminou em Empate\033[m')
        victory = True


#Shows the menu to player
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
            choose_difficulty()
            while not victory:
                player()
                show_board(board,0)
                check_victory()
                print('===============')
                if not victory:
                    tie()
                    if not victory:
                        difficulty(dif,sense,column)
                        show_board(board,0)
                        check_victory()
                        print('''\033[33m--------------
Próxima rodada
--------------\033[m''')
            if victory:
                rep = input(('Deseja continuar jogando? [S/N] '))
                while not rep in 'SsNn':
                    rep = input(('Deseja continuar jogando? [S/N]'))
                if rep in 'sS':
                    dif = 0
                    menu = 0
                    victory = False
                    board = [['-' for c in range(3)]for x in range(3)]
                if rep in 'nN':
                    main = False
                    break
    if menu == 2:      
        instruction_board = [['1,1','1,2','1,3'],['2,1','2,2','2,3'],['3,1','3,2','3,3']]
        print('''\033[1;35mO jogador utilizará o X enquanto o Computador o O
Irá sair vitorioso o primeiro a ter concluído o tabuleiro de forma horizontal, vertical ou diagonal
O tabuleiro irá seguir o seguinte padrão \033[m''')
        show_board(instruction_board,6)
    if menu == 3:
        break