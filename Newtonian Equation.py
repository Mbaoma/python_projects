#Newtonian equation
#root_of_num = 0.5 * ((num / guess) + guess)
import math
num = int(input("Enter the positive whole number you want to find the square-root of: "))
guess = int(input("Enter a positive numeric guess: "))
root_num = 0 
sqrt_num = math.sqrt(num) 
while True:
    root_num = 0.5 * ((num / guess) + guess)
    print(root_num)
    while guess != num:
        guess = root_num #for continuity reasons, we set the guess value to the root value we got earlier
        new_root = 0.5 * ((num / guess) + guess)
        print(new_root)
        break
    if new_root == sqrt_num: #a stopping criteria
            break
        
    


      
    
     
