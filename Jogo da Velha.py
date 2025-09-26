from random import randrange

def tabuleiro():#tabuleiro do jogo da vela
  print("+-------+-------+-------+")
  print("|       |       |       |")
  print("|  ",matrix[0][0] ,"  |  ",matrix[0][1] ,"  |  ",matrix[0][2] ,"  |")
  print("|       |       |       |")
  print("+-------+-------+-------+")
  print("|       |       |       |")
  print("|  ",matrix[1][0] ,"  |  ",matrix[1][1] ,"  |  ",matrix[1][2] ,"  |")
  print("|       |       |       |")
  print("+-------+-------+-------+")
  print("|       |       |       |")
  print("|  ",matrix[2][0] ,"  |  ",matrix[2][1] ,"  |  ",matrix[2][2] ,"  |")
  print("|       |       |       |")
  print("+-------+-------+-------+")  

def jogada_certa(jogada, pessoa): #verificação de jogada e jogada
    while True:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                # Se a posição corresponde à jogada
                if jogada == matrix[i][j]:
                    # Se a posição já está ocupada
                    if matrix[i][j] in ["X", "O"]:
                        if pessoa:
                            jogada = int(input("Jogada inválida, jogue novamente: "))
                        else:
                            jogada = randrange(1, 10)
                        break  
                    if pessoa:
                        matrix[i][j] = "O"
                        return False
                    else:
                        matrix[i][j] = "X"
                        return False
        else:
            if pessoa:
                jogada = int(input("Jogada inválida, jogue novamente: "))
            else:
                jogada = randrange(1, 10)

def vitoria():#verificação de vitoria 
    #Vitoria do usuario
    if matrix[0][0] == "O" and matrix[1][0] == "O" and matrix[2][0] == "O":
        print("Voce venceu")
        tabuleiro()
        return True
    elif matrix[0][1] == "O" and matrix[1][1] == "O" and matrix[2][1] == "O":
        print("Voce venceu")
        tabuleiro()
        return True        
    elif matrix[0][2] == "O" and matrix[1][2] == "O" and matrix[2][2] == "O":
        print("Voce venceu")
        tabuleiro()
        return True
    elif matrix[0][0] == "O" and matrix[0][1] == "O" and matrix[0][2] == "O":
        print("Voce venceu")   
        tabuleiro()       
        return True
    elif matrix[1][0] == "O" and matrix[1][1] == "O" and matrix[1][2] == "O":
        print("Voce venceu")
        tabuleiro()      
        return True
    elif matrix[2][0] == "O" and matrix[2][1] == "O" and matrix[2][2] == "O":
        print("Voce venceu")
        tabuleiro()       
        return True
    elif matrix[0][0] == "O" and matrix[1][1] == "O" and matrix[2][2] == "O":
        print("Voce venceu")
        tabuleiro()     
        return True
    elif matrix[0][2] == "O" and matrix[1][1] == "O" and matrix[2][0] == "O":
        print("Voce venceu")
        tabuleiro()       
        return True
    
    #Vitoria do pc
    if matrix[0][0] == "X" and matrix[1][0] == "X" and matrix[2][0] == "X":
        print("Computador venceu")
        tabuleiro()        
        return True
    elif matrix[0][1] == "X" and matrix[1][1] == "X" and matrix[2][1] == "X":
        print("Computador venceu")
        tabuleiro()        
        return True
    elif matrix[0][2] == "X" and matrix[1][2] == "X" and matrix[2][2] == "X":
        print("Computador venceu")
        tabuleiro()       
        return True
    elif matrix[0][0] == "X" and matrix[0][1] == "X" and matrix[0][2] == "X":
        print("Computador venceu")  
        tabuleiro()    
        return True
    elif matrix[1][0] == "X" and matrix[1][1] == "X" and matrix[1][2] == "X":
        print("Computador venceu")
        tabuleiro()     
        return True
    elif matrix[2][0] == "X" and matrix[2][1] == "X" and matrix[2][2] == "X":
        print("Computador venceu")
        tabuleiro()        
        return True
    elif matrix[0][0] == "X" and matrix[1][1] == "X" and matrix[2][2] == "X":
        print("Computador venceu")
        tabuleiro()        
        return True
    elif matrix[0][2] == "X" and matrix[1][1] == "X" and matrix[2][0] == "X":
        print("Computador venceu")
        tabuleiro()        
        return True
    else:
        return False        

def empate():#verificação se deu empate
    for i in range(3):
        for j in range(3):
            if matrix[i][j] in [1,2,3,4,5,6,7,8,9]:
                return False  # ainda existe posição livre
    print("Deu velha!")
    tabuleiro()
    return True

def jogo_da_velha(): #aonde o jogo é feito
 try:
     global matrix
     matrix = [[1,2,3],[4,"X",6],[7,8,9]]

      
     while True:
         

         
         if vitoria() or empate():
             break
        
        
         tabuleiro()
         jogada = int(input("Digite seu movimento:"))
         jogada_certa(jogada,True)
        
         if vitoria() or empate():
             break
        
        
         jogada_pc = randrange(1, 10)
         jogada_certa(jogada_pc,False)
         
 except:#Caso Insira algum valor errado
     print("Valor não é inteiro")

     
#EXECUÇÃO DO PROGRAMA
jogo_da_velha()