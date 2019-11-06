def absolute(x):
	if x < 0:
		print (-x)
	else:
		print(x)
absolute(-6)
print("--------------------")
''' write a compare function that returns
 1, for x>y
 0, for x==y
 -1, for x<y
 '''
def compare(x,y):
	if x > y:
		print(1)
	elif x==y:
		print(0)
	else:
		print(-1)
x,y= eval(input('enter a number: '))
compare(x,y)
print('-------------------')
def GOAT():
	topdawg= 'Lamar'
	print(topdawg)
GOAT()
print('-------------------')
'''
boolean function
boolean is an inbuilt python function that prints True or False depending on the given condition '''
print(4%2 == 0)
print(6%4 == 0)
#below is a boolean function
def yesno(a,b):
	if a%b == 0:
		print('True')
	else:
		print('False')
a,b= eval(input('enter 2 numbers seperated by comma'))
yesno(a,b)
print('-------------------')

