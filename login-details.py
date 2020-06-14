#makes use of the user defined studentlogin module

import studentlogin

def main(): 
    
    first_name = input('Enter your first name: \n')
    last_name = input('Enter your last name: \n')
    id_number = input('Enter your ID number: \n')

    print('Your student login name is:')
    print(studentlogin.login_name(first_name, last_name, id_number))
    
    password = input('Type in your password: ')
    while not studentlogin.passwords(password):
        print('invalid password')
        password = input('Type in your password: ')
    print('valid password')
    

main()
