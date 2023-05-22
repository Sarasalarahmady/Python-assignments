from pyfiglet import Figlet
def show():
    for row in game_board:
        for cell in row:
          print(cell, end="")
        print()
def check_game():
      if game_board[0][0]=="x" and game_board[0][1]=="x" and game_board[0][2]=="x":
          print("player1 wins")
         
      if game_board[1][0]=="x" and game_board[1][1]=="x" and game_board[1][2]=="x":
          print("player1 wins")
      
      if game_board[2][0]=="x" and game_board[2][1]=="x" and game_board[2][2]=="x":
          print("player1 wins")
      if game_board[0][0]=="x" and game_board[1][0]=="x" and game_board[2][0]=="x":
          print("player1 wins")
      if game_board[0][1]=="x" and game_board[1][1]=="x" and game_board[2][1]=="x":
           print("player1 wins")
      if game_board[0][0]=="x" and game_board[1][1]=="x" and game_board[2][2]=="x":
           print("player1 wins")
           return 1
      if  game_board[0][2]=="x" and game_board[1][1]=="x" and game_board[2][0]=="x":
           print("player1 wins")

          
def check_win_player2():
     
      if game_board[0][0]=="O" and game_board[0][1]=="O" and game_board[0][2]=="O":
          print("player2 wins")
          
      if game_board[1][0]=="O" and game_board[1][1]=="O" and game_board[1][2]=="O":
          print("player2 wins")
      if game_board[2][0]=="O" and game_board[2][1]=="O" and game_board[2][2]=="O":
          print("player2 wins")
      if game_board[0][0]=="O" and game_board[1][0]=="O" and game_board[2][0]=="O":
          print("player2 wins")
        
      if game_board[0][1]=="O" and game_board[1][1]=="O" and game_board[2][1]=="O":
           print("player2 wins")
      if game_board[0][0]=="O" and game_board[1][1]=="O" and game_board[2][2]=="O":
           print("player2 wins")
      if  game_board[0][2]=="O" and game_board[1][1]=="O" and game_board[2][0]=="O":
           print("player2 wins")  
game_board = [["-" , "-" , "-"],
              ["-" , "-" , "-"],
              ["-" , "-" , "-"]]
show()
while True:
    print("Player1")
    while True:
         row= int(input("Enter row: "))
         col= int(input("Enter col: "))
         if 0<= row <=2 and 0<= col <=2:
            if game_board[row][col]== "-":
                game_board[row][col] = "x"
                break
            else:
                print("select another cell ")
         else: 
            print("Enter anather cell : ")
    else:
        print("select in 0_2 :")
    show()
check_win_player1()
print("plyer2")
if check_win_player1()!= and check_win_player2!=1:
    while True:
        row= int(input("Enter row: "))
        col= int(input("Enter col: "))
        if 0<= row <=2 and 0<= col <=2:
                    if game_board[row][col]== "-":
                        game_board[row][col] = "o"
                        break
        else:
                    print("select another cell ")
    else:
                print("Enter in 0_2 : ")
    show()