#a module that generates login details for a student

#a student's login name, should consist of:
# - first three letters of the first name
# - first three letters of the last name
# - last three letters of ID number

def passwords(password):
    length = False
    uppercase_letter = False
    lowercase_letter = False
    digit = False

    #check if input is of length 7 or greater
    if len(password) >= 7:
        length = True
        for char in password:
            #check if input contains an uppercase letter
            if char.isupper():
                uppercase_letter = True
            #check if input contains a lowercase letter
            if char.islower():
                lowercase_letter = True
            #check if input contains a number
            if char.isdigit():
                digit = True
    
    if length and uppercase_letter and lowercase_letter and digit:
        valid_password = True
        
    else:
        valid_password = False
    
    return valid_password

