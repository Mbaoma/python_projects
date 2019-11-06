'''
We can print out individual letters of a word by knowledge of it's index'''
word= 'Homophobic'
letter= word[0]
print(letter)
'''to print the length of the word, we use the len- a built im function'''
print(len(word))
'''we can print the word in reverse'''
print(word[::-1])
print('-----------------')
'''let us print the letters of a word on individual lines'''
a= 'exercise'
index= 0
while index < len(a):
	z= a[index]
	print(z)
	index= index+1
'''
index= 0
len(a)= 8
z= exercise(0th)
index= increase by 1, until the 7th index, which is the 8th letter'''
print('--------------------')
a= 'goat'
index= -1
while index < len(a):
	z= a[index]
	print(z)
	index= index-1
	
a= 'nurses run'
b= a.replace(" ", "")
if b[::-1] == 'nursesrun':
	print("palindrome")
else:
	print("no")