import threading

def add(a,b):
    print(a+b)
    print(" ")

def sub(a,b):
    print(a-b)
    print(" ")

def multi(a,b):
    print(a*b)
    print(" ")

def div(a,b):
    print(a/b)
    print(" ")

x=5
y=10

t1 = threading.Thread(target = add,args = [x,y])
t2 = threading.Thread(target = sub,args = [x,y])
t3 = threading.Thread(target = multi,args = [x,y])
t4 = threading.Thread(target = div,args = [x,y])

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

print("The Calculation is Done ")

