#ReadMe: code compilation based on thinkpython's 'strings' chapter
'''
We can print out individual letters of a word by knowledge of it's index'''
word= input("Enter a word: ")
index= int(input("Enter a number within length of string: "))
letter= word[index]
print("The letter in index", index, "is",letter)
'''to print the length of the word, we use the len- a built im function'''
print("The word has", len(word), "characters")
#we can print the word in reverse
print("The word in reverse is," , word[::-1])
print('-----------------')

'''let us print the letters of a word on individual lines'''
word = 'exercise'
index= 0
while index < len(word):
	z= word[index]
	print(z)
	index= index+1
'''
index= 0
len(a)= 8
z= exercise(0th)
index= increase by 1, until the 7th index, which is the 8th letter'''
print('--------------------')

#print out the letters on a line in reverse order
word = input("Enter a word: ")
index= -1
length= len(word) -1
#for loop
for i in range(len(word)): 
	z= word[index]
	print(z)
	index = index - 1
#while loop
while length >= 0:
	z= " "
	z = z + word[length]
	length = length - 1
	print(z)
print('_---------------------')

#Palindrome checks	
word = input("type a word: ")
b= word.replace(" ", "")
if b[::-1] == b:
	print(word, "is a palindrome")
else:
	print(word, "is not a palindrome")
print('--_-------------------')

#Strings are immutable, i.e: you can't alter them, buttttt.......
word= 'He likes playing football'
new_word= 'She' + word[2: ] #specify last index value of the word you want to replace
print(new_word)
print("--_-------------------------")

#to check the indicies of a character in a string
def find_char(word,letter):
	index = 0
	while index < len(word):
		if word[index] == letter:
			print("the letter", letter, "can be found in the following index positions", index)
		else:
			print("letter", letter, "is not in string")
		index = index + 1
word = "Mississippi"
letter= "s" 
find_char(word,letter)
print("---------------------------------")

#how many of a particular letter are in a word
word= "Regenerate"
for i in word:
	count= 0
	letter= 'e'
	if i == letter:
		count = count+1
		print("The letter", letter,"appears", count,"times")
		print(sum(count))
print("--------------------------------")

#code that checks if a given word spelt backwards gives another word
def reversal(word1,word2):
	if len(word1) != len(word2):
		print ("Word not reversible")
	i = 0
	j = len(word2) - 1
	while j > 0:
		print(i,j)
		if word1[i] != word2[j]:
			print("Not reversible")
		i = i + 1
		j = j - 1
		print("Reversible")
word1 = input("Enter a word: ")
word2= input("Enter a word: ")
reversal(word1,word2)
print("------------------------------")

print("The original word is encrypted by moving 7 places from the original alphabet")
word= input("Enter a word: ")
word= word.lower() #accepts input
step_value = int(input("Enter a step value: "))
for i in word: #isolates the letters in the string
	if i in word: #checks if the isolated letters are in the given string
		p = ord(i) + step_value #increases the numerical value of the characters
		print(chr(p)) #print new characters after adding step value
print("----------------------------------")

'''
#code to arrange words in alphabetical order
'''
word1= input("Enter a word: ")
word1 = word1.upper()
word2 = input("Enter a word: ")
word2 = word2.upper()
if word1 < word2:
	print(word1, "comes before", word2)
elif word1 > word2:
	print(word2, "comes before", word1)
else:
	print(word1, "equals", word2)
print("--------------------------")

# Program to sort alphabetically the words provided by the user
# To take input from the user
my_str = input("Enter words seperated by space: ")
# breakdown the words into a list
words = my_str.split()
# sort the list
words.sort()
# display the sorted words
print("The sorted words are: ")
for i in words:
   print(i)