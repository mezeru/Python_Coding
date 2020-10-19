from operator import ixor
from functools import reduce



def xor(arr):
    res = reduce(lambda x,y: x^y ,arr)         # Applying XOR on all the elements in the List 
    if res:
        print(arr)                             # Printing the arrays with max XOR output

    


    

def genNum(no,max,arr,i):


    if i == no:                                 # At the last Position 
        count = 0                      
        for i in arr:                           # Iterating through the array for finding the number of max bits
            count = count + i
        if count <= max:                        # Checking the condition 
            xor(arr)                            # Calling function to apply XOR Function
        return

    else: 
        arr[i] = 0                              # Set all intial positions to 0  
        genNum(no,max,arr,i+1)                  # Recursively call genNum for next position  
        arr[i] = 1                              # Set the next position to 1
        genNum(no,max,arr,i+1)

        


if __name__ == "__main__":
    
    print("Enter the no. of bits : ",end="")   # Enter the Number of bits
    no = int(input())

    print("Enter the max bits : ",end="")      # Enter the Number of Max Bits
    max = int(input())
    arr = [0]*no                        # Initialising a list for generating Binary Numbers 

    genNum(no,max,arr,0)
    
 
