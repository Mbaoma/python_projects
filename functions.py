'''the word in bracket is called argument. The function takes an argument'''
def print_twice(walter):
	print(walter)
	print(walter)
print_twice('i like u')
print('+------------------+')

def lyric():
	'''empyty parenthesis means the function takes no argument'''
	print('Lately, ive been thinking')
def lyrics():
	print('i want you to be happier')
def full_lyric():
	'''the final result would compose of the resukts of two functions'''
	lyric()
	lyrics()
	lyrics()
full_lyric()
print('+-----------------+')

def local_variable(line1, line2):
	'''assign a variable in a function(variable is called local variable)'''
	local= line1 + line2
	print(local)
	print(local)
	'''print shows how many times the result will be displayed'''
line1= "everything comes back around"
line2= "bang, bang, boomerang"

local_variable(line1,line2)
print('+--------------------+')

