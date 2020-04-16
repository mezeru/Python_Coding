import random
import os

plrwin=None
cmpwin=None
first=None
bof=None
bo=[" "," "," "," "," "," "," "," "," "," "," "," "]
plr=None
cmp=None

def compmovemade():  #entring computer's move in the board
    move=commove()
    if move!=None:
        moveismade(bo,move,cmp)
        PB()
    
    return checkwinner(bo,cmp)
def checkbof(): #checks if board is full
    global bof
    if " " not in bo:
        bof=True

def commove():  #Computer's move is decided
 global bo

 for i in range(1, 10):
    vbo = bocpy()
    if space(i,vbo):
        moveismade(vbo,i,cmp)
        if checkwinner(vbo,cmp):
               return i
 

 for i in range(1, 10):
    vbo = bocpy()
    if space(i,vbo):
        moveismade(vbo,i,plr)
        if checkwinner(vbo,plr):
              return i
                 
       
 mv=movesavailable(bo,[1,3,7,9])
 if mv==None:
        if space(5,bo):
            return 5
        else:
            mv=movesavailable(bo,[2,4,6,8])
            return mv

 else:
        return mv

def movesavailable(board,lis):#spaces avilable for the computer to make move Returns a random move if moves are avilable else returns Non
    global bo
    possible=[]
    for i in lis:
        if space(i,bo):
            possible.append(i)
    if len(possible) != 0:
        return random.choice(possible)
    else:
        return None
        
def bocpy(): #copy of board is created for trial of outcomes
    vbo = []
    for i in bo:
       vbo.append(i)
    return vbo
    
def checkwinner(bo,s):#Checks if the GAME has been won and returns 1 is Won
    return  ((bo[7] == s and bo[8] == s and bo[9] == s) or (bo[4] == s and bo[5] == s and bo[6] == s) or (bo[1] == s and bo[2] == s and bo[3] == s) or (bo[7] == s and bo[4] == s and bo[1] == s) or (bo[8] == s and bo[5] == s and bo[2] == s) or(bo[9] == s and bo[6] == s and bo[3] == s) or(bo[7] == s and bo[5] == s and bo[3] == s) or(bo[9] == s and bo[5] == s and bo[1] == s))

def space(pos,board): #checks if space on board is occupied or not
    return board[pos]==" "

def moveismade(bor,pos,sign): #assigns the move on the board
     bor[int(pos)]=sign
    

def PB():#Prints Board
    print(bo[1]+"|"+bo[2]+"|"+bo[3])
    print("-+-+-")
    print(bo[4]+"|"+bo[5]+"|"+bo[6])
    print("-+-+-")
    print(bo[7]+"|"+bo[8]+"|"+bo[9])
    print("\n\n")

def plrin():  #inputs PLayer input into the board
    while True:
        global bo
        print("Where do you want to put your "+plr)
        plrinp=input()
        if plrinp in ['1','2','3','4','5','6','7','8','9']:
              
               if False == space(int(plrinp),bo):
                     print("The Position is atready occupied , Please choose another Position ")
                     continue
               else:
                   break
          
        else:
               print("Please Type in a number betwen 1-9 ONLY\n\n")
               continue

    moveismade(bo,plrinp,plr)
    PB()
    return checkwinner(bo,plr)#checks if the player has won after the input
    

def firstone(): #decides who goes first
    first=random.randint(1,2)
    if first==1:
        print("You can GO First")
        
    else:
        print("Computer will GO First")

    return first

        
def pfirstinput(): #player chooses if he/she wants 'X' or 'O'
    while True:
        global plr
        global cmp
        print("DO you want 'X' or 'O' ")
        plr=input().upper()
        if plr == 'X' or plr == 'O':
            break
        else:
            print("Please Enter 'X' or 'O' only , try again \n\n")
            continue
    print("You have chosen "+plr)

    if plr == 'X':
        return 'O'
    if plr == 'O':
        return 'X'
        


print("Welcome To TIC - TAC - TOE")

while True :
    
    cmp = pfirstinput()
    first=firstone()
    while True:

        if first==1:
            plrwin=plrin()
            cmpwin=compmovemade()
            checkbof()
            if bof==True or plrwin==True or cmpwin==True:
                break
        else:
            cmpwin=compmovemade()
            plrwin=plrin()
            checkbof()
            if bof==True or plrwin==True or cmpwin==True:
                break
            
             

    if(plrwin == True):
        print("You Won !!!!!")
    

    elif(bof==True):
        print("The Game is Draw")
    

    elif cmpwin==True:
      print("\nThe computer WON !!")

    print("DO You want to play again ?")
    c=input()
    if (c).upper == 'Y':
        break
    os.system('cls')
    
    


        
