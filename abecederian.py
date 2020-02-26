prefix= 'ABCDFGHJKLMNOPQRSTUVWXYZ'
for letter in prefix:
	suffix = 'ack'
	if letter == 'O' or letter== 'Q':
		suffix= 'uack'
		print(letter + suffix)
	else:
		print(letter + suffix)
