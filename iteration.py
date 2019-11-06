'''
In python, a variable can be assigned more than one value'''
a= 8
print(a)
a= 9
print(a)
print('--------------')

'''An update on a variable can also be done'''
x= 3
x= x+1
print(x)
print('----------------')

''' While statements are used for repetitive tasks, the underlying code prints Sam for everytime the value of the variable s, is greater than 0'''
def the_one(s):
	while s > 0:
		print('Sam')
		s= s-1
the_one(6)
print('----------------')

'''
A Newtonian equation to solve for square root of a number- y=x+(a/x)/2
'''
while True:
	a= int(input("what number\'s square root do you seek?: "))
	x= 3
	y= (x+ a/x) / 2
	print(y)
	if x==y:
		break
	x = y
	break
	