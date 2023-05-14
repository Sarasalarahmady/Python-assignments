def draw_chessboard(m , n) :
    for row in range(m):
        board= ""
        for column in range (n):
            if n % 2 ==0:
                board += "#*"
            else:
                board += "*#"
        print(board)
m = int(input(" Enter m : "))
n = int(input(" Enter n : "))
# print("\n")
draw_chessboard(n,m)