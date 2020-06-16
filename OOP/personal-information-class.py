#Design a class that holds the following personal data: name, address, age, and phone number.
#Write appropriate accessor and mutator methods. Also, write a program that creates an
#instance of the class. One instance should hold your information, and the other  
# should hold another person's information

class Personal_Information:
    def __init__ (self, name, address, age, phone):
        self.__yourname = name
        self.__youraddress = address
        self.__yourage = age
        self.__yourphone = phone
    
    def set_your_name(self, name):
        self.__yourname = name
    
    def set_your_address (self, address):
        self.__youraddress = address
    
    def set_your_age (self, age):
        self.__yourage = age
    
    def set_your_phone (self, phone):
        self.__yourphone = phone
    
    def get_your_name (self):
        return self.__yourname
    
    def get_your_address (self):
        return self.__youraddress
    
    def get_your_age (self):
        return self.__yourage
    
    def get_your_phone (self):
        return self.__yourphone

def main():
    name = input('What is your name: ')
    address = input('Where do you live: ')
    age = int(input('How old are you: '))
    phone = (input('Type your number: '))

    my_info = Personal_Information(name, address, age, phone)
    print('MY INFO')
    print('Hi, I am ', my_info.get_your_name())
    print('I live at ', my_info.get_your_address())
    print('I am ', my_info.get_your_age(), ' years old')
    print('Contact me via ', my_info.get_your_phone())

    
main()



    
