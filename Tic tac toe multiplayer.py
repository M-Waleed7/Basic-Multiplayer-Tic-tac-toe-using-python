# Tick tac toe game assignment 4
#Name:M.Waleed
#Reg no:Fa21-bds-014
#subject:ICT

# creating a board 
board=[['-', '-', '-'],
       ['-', '-', '-'],
       ['-', '-', '-']]
#making board function in 2d
def draw_board():
    for i in range(3):
        print()
        for j in range(3):
            print(board[i][j],end="")
            if j<2:
                print("|",end="")
#making a toss using random function
def toss():
    player1=input('enter player one name=')
    player2=input('enter player two name=')
    import random
    print('toss for the turn')
    print('1 for heads \n2 for tales')
    p1=eval(input('enter toss value'))
    toss=random.randint(1,2)
    if toss==1:
        print(player1,end="")
        print(' won the toss')
    else:
        print(player2,end="")
        print(' won the toss')
#taking input from the user and storing it in pos
def user_input():
    pos=eval(input("\nenter the number where you want to place=="))
    pos=pos-1
    return pos
#By using user input finding row and coloumn to place symbol there
def place_player1(pos):
    row=pos//3
    coloumn=pos%3
    board[row][coloumn]='X'
    if win_condition('X'):
        print("congratulation player1 wins the game")
        exit()
    tie_condition()
# similarly for player2
def place_player2(pos):
    row=pos//3
    coloumn=pos%3
    board[row][coloumn]='O'
    if win_condition('O'):
        print("congratulation player2 wins the game")
        exit()
    tie_condition()
# making a tie condition     
def tie_condition():
    k=0
    for i in range(3):
        for j in range(3):
            if board[i][j]!="-":
                k=1
            else:
                 k=0
    if k==1:
        print("your game is tied")
        exit()
# creating win condition to check if user wins or not
def win_condition(mark):
    
    if(board[0][0]==board[0][1]==board[0][2]==mark):
        return True
    elif(board[1][0]==board[1][1]==board[1][2]==mark):
        return True
    elif(board[2][0]==board[2][1]==board[2][2]==mark):
        return True
    elif(board[0][0]==board[1][0]==board[2][0]==mark):
        return True
    elif(board[0][1]==board[1][1]==board[2][1]==mark):
        return True
    elif(board[0][2]==board[1][2]==board[2][2]==mark):
        return True
    elif(board[0][0]==board[1][1]==board[2][2]==mark):
        return True
    elif(board[0][2]==board[1][1]==board[2][0]==mark):
        return True
    else:
        return False
#place where the program start
def main():
    print("_______________________________")
    print("|  Welcome to Tic Tac Toe Game |")
    print("|_____________________________ |\n")
    toss()
    #displaying the board for instruction
    print('1 |2 |3')
    print('__|__|___')
    print('4 |5 |6')
    print('__|__|___')
    print('7 |8 |9')
    print()
    print('To place ,You have to select the number from 1 - 9')
    game_on=True
    while game_on:
        #calling all the functions in sequence
        draw_board()
        pos=user_input()
        place_player1(pos)
        draw_board()
        pos=user_input()
        place_player2(pos)
             
main()



