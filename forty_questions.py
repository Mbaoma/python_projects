#script that based on the number of players,
#slices the total number of questions equally among the players
# it does all assigning randomly too 

import random 
import pprint

def question_numbers(l,players):
    for i in range(0, 40, players):
        yield l[i: i + players]
players = 8
names = ['weirdo','shey proper','omarrr','aunt chizi','vykybobo']
random.shuffle(names)
num = list(question_numbers(range(1,40,), players))
random.shuffle(num)
for i,j in (zip(names,num)):
    print(i,j, end= ',')
