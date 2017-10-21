import numpy as np

mapa = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
is_active = True
vez = 1
velha = 0
while is_active:
    if vez%2 == 1:
        print("\n[!] VEZ DO O!\n")
        col_s = input("[?] Qual sua jogada? Escreva a coluna aonde você quer colocar o seu X ou O.\n")
        lin_s = input("[?] Agora coloque a linha!\n")
        col = int(col_s) - 1
        lin = int(lin_s) - 1
        if mapa[lin][col]!=' ':
            print("\n[!!] Parece que você colocou em uma posição que já havia sido preenchida. Vamos tentar denovo!\n")
            continue
        else:
            mapa[lin][col] = 'O'
        print(np.matrix(mapa))
        if mapa[0][0] != ' ' and mapa[1][1] == mapa[0][0] and mapa[2][2] == mapa[0][0]:
            print("[!] Parabéns! O "+str(mapa[1][1])+" ganhou!\n")
            is_active = False
        if mapa[0][2] != ' ' and mapa[1][1] == mapa[0][2] and mapa[2][0] == mapa[0][2]:
            print("[!] Parabéns! O "+str(mapa[1][1])+" ganhou!\n")
            is_active = False
        for i in mapa:
            if i[0] != ' ' and i[0] == i[1] and i[1] == i[2]:
                print("[!] Parabéns! O "+str(i[0])+" ganhou!\n")
                is_active = False
        for i in range(0,2):
            if mapa[0][i] != ' ' and mapa[0][i] == mapa[1][i] and mapa[1][i] == mapa[2][i]:
                print("[!] Parabéns! O "+str(mapa[0][i])+" ganhou!\n")
                is_active = False
        for i in range(3):
            for j in range(3):
                if mapa[i][j] != ' ':
                    velha += 1
        if velha == 9:
            print("[!] Deu velha!")
            is_active = False
        velha = 0
    else:
        print("\n[!] VEZ DO X!\n")
        col_s = input("[?] Qual sua jogada? Escreva a coluna aonde você quer colocar o seu X ou O.\n")
        lin_s = input("[?] Agora coloque a linha!\n")
        col = int(col_s) - 1
        lin = int(lin_s) - 1
        if mapa[lin][col]!=' ':
            print("\n[!!] Parece que você colocou em uma posição que já havia sido preenchida. Vamos tentar denovo!\n")
            continue
        else:
            mapa[lin][col] = 'X'
        print(np.matrix(mapa))
        if mapa[0][0] != ' ' and mapa[1][1] == mapa[0][0] and mapa[2][2] == mapa[0][0]:
            print("[!] Parabéns! O "+str(mapa[1][1])+" ganhou!\n")
            is_active = False
        if mapa[0][2] != ' ' and mapa[1][1] == mapa[0][2] and mapa[2][0] == mapa[0][2]:
            print("[!] Parabéns! O "+str(mapa[1][1])+" ganhou!\n")
            is_active = False
        for i in mapa:
            if i[0] != ' ' and i[0] == i[1] and i[1] == i[2]:
                print("[!] Parabéns! O "+str(i[0])+" ganhou!\n")
                is_active = False
        for i in range(0,2):
            if mapa[0][i] != ' ' and mapa[0][i] == mapa[1][i] and mapa[1][i] == mapa[2][i]:
                print("[!] Parabéns! O "+str(mapa[0][i])+" ganhou!\n")
                is_active = False
        for i in range(3):
            for j in range(3):
                if mapa[i][j] != ' ':
                    velha += 1
        if velha == 9:
            print("[!] Deu velha!")
            is_active = False
        velha = 0
    vez += 1
