import random
import os
import time

hangdraw=0
hangman=['''
 +---+
     |
     |
     |
    ==='''
,'''
 +---+
 O   |
     |
     |
    ==='''
,'''
 +---+
 O   |
 |   |
     |
    ==='''
,'''
 +---+
 O   |
/|   |
     |
    ==='''
,'''
 +---+
 O   |
/|\  |
     |
    ==='''
,'''
 +---+
 O   |
/|\  |
/    |
    ==='''
,'''
 +---+
 O  |
/|\ |
/ \ |
    ==='''
]


def lose():
    print("The word was '"+rword+"'")
    print("The letters missed where : ")
    for i in range(len(rword)):
        if rword[i] not in Gboard:
            print(rword[i]+" ",end='')
    print("\n")


def checkpinput(int): #checks if input is a letter
    if int not in 'abcdefghijklmnopqrstuvwxyz':
        return False
    elif int in Sminput:
        return True
    elif len(int)!=1:
        return 1
    else:
        Sminput.append(int)
                   

def Gboardedit(rword): #Board for the words
    for i in range(len(rword)):
        Gboard.append('_')

words = 'Apple Boy Cat Dog Elephant Fox Girl Horse Ice Jackal Kangaroo'.split() #string is used instead of lidts to find no. of words 

def getword():  #Chooses a random word
 a=random.randint(0,len(words)-1)
 return words[a]


def inword(int,rword): #checks if input is there or not in the word
    int.lower()
    
    if int in rword:
        for i in range(len(rword)):
            if rword[i] == int:
                Gboard[i]=int
                
               
    else :
        global hangdraw
        hangdraw=hangdraw+1

    print(hangman[hangdraw])
          
    for i in range(0,len(rword)):
        print(Gboard[i]+" ",end='')
    print("\n\n")
    

print('''
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝

                                                                \n''')
time.sleep(2)
print("How to Play \n1)You have to Guess The Word Given word by word \n2)You have Six Chances \n3)Have Fun !!\n\n\n\n")
time.sleep(5)
os.system('cls')      
 
while True:
    Gboard=[]
    Sminput=[]
    rword=getword()
    Gboardedit(rword)
    print(hangman[0])
    for i in range(len(rword)):
        print(Gboard[i]+" ",end='')
    print()
  
    while True:
        if hangdraw < 6:
            print("\nEnter a Letter : ")
            ltr=input()
            ckin=checkpinput(ltr)
            if ckin == False:
                print("\nEnter a Letter please , Try Again")
                continue
        
            elif ckin == True:
                print("\nYou have entered The same Letter , Try Again")
                continue
        
            elif ckin == 1:
                print("\nPlease enter only one Letter , Try Again")
                continue
        
            else:
                inword(ltr,rword)
                
            if '_' not in Gboard:
                print("You Won !! Congrats ")
                break
    
        else:
            print("You Lose !!")
            lose()
            break

        
    os.system('cls')   
    print("Do you want to play again ? ")
    choice=input()
    if choice =='Y' or choice =='YES'or choice =='y' or choice =='yes':
        Gboard.clear()
        Sminput.clear()
        hangdraw=0
        os.system('cls')
        continue

    else:
        break
        

        
    

        
