#yaay, let's play z guessing game
from random import randint
import sys
num = randint(int(sys.argv[1]),int(sys.argv[2]))
# when you run your code from the terminal ... as follows :
# python game.py , pass in the sys arguments immediately as follows (for example if you want a number between 1 and 20):
# python game.py 1 20..
while True:  
    try:
        user_guess = int(input("Enter a number between 1 and 10: "))
        if user_guess > 0 and user_guess < 11 :
            if user_guess == num:
                print("you\'re a geni dude")
                break
        else:
            print('Alaye, enter a number between 1 and 10')
    except ValueError:
        print('Please enter a number between 1 and 10:')
