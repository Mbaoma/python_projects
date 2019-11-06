prefix= 'ABCD:FGHJKLMNOPQRSTUVWXYZ'
for letter in prefix:
	suffix = 'ack'
	if letter == 'O' or letter== 'Q':
		suffix= 'ouack'
		print(letter + suffix)
	else:
		print(letter + suffix)