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
	
