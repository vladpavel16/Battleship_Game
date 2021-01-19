
##Battleship game for 2 players with a maximum of 10 turns to play(each player can hit for 10 times).
##Solution was implemented based on the course from https://erlerobotics.gitbooks.io/erle-robotics-learning-python-gitbook-free/exercisebattleship/battleship.html
##Additional contribution was by making the game multiplayer for 2 with a preferable number(that can be reset) of rounds to play

from random import randint
                            ##initialize 2 playing boards with "O"s for 5 rows and 5 collumns;
board1=[]                   ##board1 is for player1
board2=[]                   ##board2 is for player2

for i in range(0,5):
    board1.append(["O"]*5)
for i in range(0,5):
    board2.append(["O"]*5)
    
def print_board(board):
    for i in board:
        print(" ".join(i))
        
print("Let's play!")
print_board(board1)
print()
print_board(board2)

#the point on board where the ship is, is generated randomly
def random_row(board):              
    return randint(0,len(board)-1)
    
def random_col(board):
    return randint(0,len(board)-1)

###setting the point for player 1's battleship on the board:    
ship_row1=random_row(board1)
ship_col1=random_col(board1)
###setting the point for player 2's battleship on the board:    
ship_row2=random_row(board2)
ship_col2=random_col(board2)

#####if you want to know where the ships are located on the boards:

##print("Coordinates of player 1's ship:")
##print(ship_row)
##print(ship_col)
##print("Coordinates of playet 2's ship:")
##print(ship_row2)
##print(ship_col2)

###the game is played for 10 turns and for each player a set of methods applies:
for turn in range(1,10):
    print("Turn:",turn)
    #It's Player 1's turn!
    print("First player's turn!")           ##Player 1 gives the coordinates to hit player 2's ship
    guess_row1=int(input("Guess Row:"))
    guess_col1=int(input("Guess Col:"))

    if (guess_row1==ship_row2) and (guess_col1==ship_col2) :        ##if he hits, the game is over, player 2 will never have the chance to hit 
        print("Congrats! You sank the player 2' ship")
        print("IT'S OVER!")
        exit()
    else:
        if turn==9:                                                 ##if the ship isn't hit and the turns end, the game ends as well
            print("Game Over!")
            exit()
        elif (guess_row1<0 or guess_row1>4) or (guess_col1<0 or guess_col1>4):  ##if the player1 gives coordinates that ar not on the board he misses the board
            print("Oups, that's not even in the ocean, you missed the board")
        elif (board2[guess_row1][guess_col1]=="X"):                             ##if the player1 hits somewhere on the board but not the ship, a "X" is assigned to that coordinates
            print("You guessed that one already")                               ## and if the player1 hits the same spot, it's the same
        else:
            print("You missed my battleship!")
            board2[guess_row1][guess_col1]="X"
        
        
    print()
    #It's Player 2's turn!
    print("Second player's turn!")         ##Player 2 gives the coordinates to hit player 1's ship 
    guess_row2=int(input("Guess Row:"))
    guess_col2=int(input("Guess Col:"))

    if (guess_row2==ship_row1) and (guess_col2==ship_col1) :        ##if he hits, the game is over, player 1 will never have the chance to hit 
        print("Congrats! You sank the player 1's ship")
        print("IT'S OVER!")
        exit()
    else:
        if turn==9:                                                 ##if the ship isn't hit and the turns end, the game ends as well
            print("Game Over!No winner :( ")
            exit()
        elif (guess_row2<0 or guess_row2>4) or (guess_col2<0 or guess_col2>4):  ##if the player1 gives coordinates that ar not on the board he misses the board
            print("Oups, that's not even in the ocean, you missed the board")
        elif (board1[guess_row2][guess_col2]=="X"):                             ##if the player 2 hits somewhere on the board but not the ship, a "X" is assigned to that
            print("You guessed that one already")                               ## and if the player 2 hits the same spot, it's the same
        else:
            print("You missed my battleship!")
            board1[guess_row2][guess_col2]="X"
            
       ###After both players have made their moves, the updated board will be printed on the screen  
        print("Player 1 board")
        print_board(board1)
        print("~~~~~~~~~~")
        print("Player 2 board")
        print_board(board2)


    
        
