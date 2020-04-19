import time



def stop():
    global st
    lp=0
    try:
        while True:
            input()
            lap=round((time.time()-st),4)
            print("Lap " +str(lp)+ " at time %s"%lap) 
            lp+=1
    except KeyboardInterrupt:
        print("\n\n")
            
            
        
    
    return time.time()

print("\nPress 'Enter' to start the stopwatch and 'Ente'r again to LAP it and press 'Ctrl + C' to stop it ")
input()

st=time.time()

ft=stop()

print("The time was stopped at : %s"%(ft-st))

time.sleep(10)
