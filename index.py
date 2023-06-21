board=["-","-","-",
       "-","-","-",
       "-","-","-"]

#player1="X"
#player2="O"
currentplayer="X"
winner=None
gamerunning=True

def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--------------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--------------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def mplayer1(board):
    pos1=int(input("Player 1 enter the position from 1-9 : "))
    if(pos1>=1 and pos1<=9 and board[pos1-1]=="-"):
        board[pos1-1]=currentplayer
    else:
        print("Position already taken.")

def mplayer2(board):
    pos2=int(input("Player 2 enter the position from 1-9 : "))
    if(pos2>=1 and pos2<=9 and board[pos2-1]=="-"):
        board[pos2-1]=currentplayer
    else:
        print("Position already taken.")

def switchplayer():
    global currentplayer
    if(currentplayer=="X"):
        currentplayer="O"
    else:
        currentplayer="X"

def horizontal(board):
    global winner
    if(board[0]==board[1]==board[2] and board[0]!="-"):
        winner=board[0]
        return True
    elif(board[3]==board[4]==board[5] and board[3]!="-"):
        winner=board[3]
        return True
    elif(board[6]==board[7]==board[8] and board[6]!="-"):
        winner=board[6]
        return True
    
def vertical(board):
    global winner
    if(board[0]==board[3]==board[6] and board[0]!="-"):
        winner=board[0]
        return True
    if(board[1]==board[4]==board[7] and board[1]!="-"):
        winner=board[0]
        return True
    if(board[2]==board[5]==board[8] and board[2]!="-"):
        winner=board[2]
        return True
    
def diagonal(board):
    global winner
    if(board[0]==board[4]==board[8] and board[0]!="-"):
        winner=board[0]
        return True
    if(board[2]==board[4]==board[6] and board[2]!="-"):
        winner=board[2]
        return True
    
def win():
    global gamerunning
    if(horizontal(board) or vertical(board) or diagonal(board)):
        print(f"{currentplayer} is the winner")
        printboard(board)
        gamerunning=False
    if(gamerunning==False):
        exit()

def tie(board):
    global gamerunning
    if("-" not in board):
        print("It's a tie.")
        gamerunning=False
        exit()

print("***********************************")
print("TIC TAC TOE")
print("***********************************")

while(gamerunning):
    printboard(board)
    mplayer1(board)
    win()
    tie(board)
    switchplayer()
    printboard(board)
    mplayer2(board)
    win()
    tie(board)
    switchplayer()