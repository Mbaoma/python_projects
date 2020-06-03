#a script that tells you the actual digits of a service custom number
#steps

# -map numbers to variables
# -make the actual alphabets equal to variables
# -ask for 10 character number seperated by '-'
#    e.g: xxx-xxx-xxxx
# -translate the service number to numeric equivalent
# -such that 555-GET-FOOD is 555-438-3663

TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT = 8
NINE = 9

def custom_service():
    custom_number = input('your number in this format: \n \
                XXX-XXX-XXXX: \n ')
    #custom_number = custom_number.upper()
    for letter in custom_number:
        custom_number = custom_number.upper()
        '''
        if letter == 'A':
            letter = letter.replace('A', str(TWO))
        
        elif letter == 'B':
            letter = letter.replace('B', str(TWO))
        
        elif letter == 'C':
            letter = letter.replace('C', str(TWO))
        
        elif letter == 'D':
            letter = letter.replace('D', str(THREE))
            
        else:
            letter = letter.replace(letter, '4')
        print(letter, end = '-')
        '''
        replace_a = custom_number.replace('A', str(TWO))
        replace_b = replace_a.replace('B', str(TWO))
        replace_c = replace_b.replace('C', str(TWO))

        replace_d = replace_c.replace('D', str(THREE))
        replace_e = replace_d.replace('E', str(THREE))
        replace_f = replace_e.replace('F', str(THREE))

        replace_g = replace_f.replace('G', str(FOUR))
        replace_h = replace_g.replace('H', str(FOUR))
        replace_i = replace_h.replace('I', str(FOUR))

        replace_j = replace_i.replace('J', str(FIVE))
        replace_k = replace_j.replace('K', str(FIVE))
        replace_l = replace_k.replace('L', str(FIVE))

        replace_m = replace_l.replace('M', str(SIX))
        replace_n = replace_m.replace('N', str(SIX))
        replace_o = replace_n.replace('O', str(SIX))

        replace_p = replace_o.replace('P', str(SEVEN))
        replace_q = replace_p.replace('Q', str(SEVEN))
        replace_r = replace_q.replace('R', str(SEVEN))
        replace_s = replace_r.replace('S', str(SEVEN))

        replace_t = replace_s.replace('T', str(EIGHT))
        replace_u = replace_t.replace('U', str(EIGHT))
        replace_v = replace_u.replace('V', str(FOUR))

        replace_w = replace_v.replace('W', str(NINE))
        replace_x = replace_w.replace('X', str(NINE))
        replace_y = replace_x.replace('Y', str(NINE))
        replace_z = replace_y.replace('Z', str(NINE))
        
    print('The numerical equivalent of ',custom_number, ' is: \n', replace_z)

custom_service()


