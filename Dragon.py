import random
import time

def intro():
    print("You wake up in a Haze. You see a that you are in a bedroom. You pick yourself up and Notice there are Two Doors to exit the Room",end='')
    print("There are Signs in front of the doors.")
    print("The sign infront of the First door says \"A Dragon Lies Here !!\"")
    print("The sign infront of the Second door says \"There is no Dragon here\"")
   

def dragon():
    return random.randint(1,2)

def Lose():
    print("You where Killed ")
    print("YOU LOSE !!")
    print("Good Day, SIR")

def win():
    print("Well YOU WIN then , I guess ")
    
    
intro()
a=dragon()

print("Which door do you choose............",end='')
b=int(input())

if (a==b):
    print("The Dragon is here ")
    
    if b==1 :
         print("The Sign was telling the truth")
    elif b==2 :
         print("The Sign was NOT telling the truth")
    Lose()
elif (a != b):
    print("The Dragon is NOT here ")
    if a==1 :
           print("The Sign was NOT telling the truth")
    if a==2 :
           print("The Sign was telling the truth")
    print("Hmmm...So you are still alive ? Well not For long, Here comes the dragon anyway")
    print("What do you do ?")
    k=input()
    if k == "kill it" or k == "KILL IT" or k == "kill" or k == "KILL":
        print("What !! You killed my pet dragon ??")
        win()
    else :
        print("Wrong !!")
        Lose()
time.sleep(15)
input()
