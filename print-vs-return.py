
#a script that shows the different results we get when we use 'print' and 'return' in python functions

#WORKING WITH 'PRINT'
def add_two_numbers(num_one, num_two): #i defined a function which is to add two numbers 
    answer = num_one + num_two #the variable name 'answer' is assigned to the intended math operation
    print(answer) #'print' statement displays the value of 'answer'
num_one = 10
num_two = 2
value = add_two_numbers(num_one, num_two)
print(value) #'print' statement displays the result of 'value'

#WORKING WITH RETURN
def add_two_numbers(num_one, num_two): #i defined a function which is to add two numbers 
    answer = num_one + num_two #the variable name 'answer' is assigned to the intended math operation
    return(answer) #'return' statement stores the value of 'answer'
num_one = 10
num_two = 2
value = add_two_numbers(num_one, num_two)
print(value) #'print' statement displays the result of 'value'

#Let's manipulate our function's value

#WORKING WITH 'PRINT'
def add_two_numbers(num_one, num_two): #i defined a function which is to add two numbers 
    answer = num_one + num_two #the variable name 'answer' is assigned to the intended math operation
    print(answer) #displays the value of 'answer'
num_one = 10
num_two = 2
num_three = 3
value = add_two_numbers(num_one, num_two) - num_three
print(value) #'print' statement displays the result of 'value'

#WORKING WITH RETURN
def add_two_numbers(num_one, num_two): #i defined a function which is to add two numbers 
    answer = num_one + num_two #the variable name 'answer' is assigned to the intended math operation
    return(answer) #'return' statement stores the value of 'answer'
num_one = 10
num_two = 2
num_three = 3
value = add_two_numbers(num_one, num_two) - num_three
print(value) #'print' statement displays the result of 'value'

#USING BOTH 'PRINT' AND 'RETURN' STATEMENTS IN A FUNCTION

#WORKING WITH RETURN
def add_two_numbers(num_one, num_two): #i defined a function which is to add two numbers 
    answer = num_one + num_two #the variable name 'answer' is assigned to the intended math operation
    return(answer) #'return' statement stores the value of 'answer'
num_one = 10
num_two = 2
print(add_two_numbers(num_one, num_two)) #'print' statement displays the result of our function
