import random

def rnum():
    return (random.randint(0,10))

fnum=rnum()

cou = 0
while True:
    print("Guesses the no :")
    cou=cou+1
    G=int(input())

    if fnum == G :
        print("You guessed right in " + str(cou)+" Guess")
        break

    
    elif fnum > G:
       print("You guessed LOW")
       continue

    
    elif fnum < G:
        print("You guessed High")
        continue   
    
    else:
        continue

