#a student's login name, should consist of:
# - first three letters of the first name
# - first three letters of the last name
# - last three letters of ID number
'''
def login_name(first_names, last_names, id_num):
    first_names = first_names[0:3]
    
    last_names = last_names[0:3]

    id_num = id_num[-3:]

    print('Your login name is, ' + first_names + last_names + id_num)

first_names = input('Enter your first name: \n')
last_names = input('Enter your last name: \n')
id_num = input('Enter your ID number: \n')

login_name(first_names,last_names,id_num)
'''
def login_name(first_name, last_name, id_number):
    first_name = first_name[0 : 3]
    last_name = last_name[0 : 3]
    id_number = id_number[-3 : ]

    login = first_name + last_name + id_number

    return login
login_name(first_name, last_name, id_number)