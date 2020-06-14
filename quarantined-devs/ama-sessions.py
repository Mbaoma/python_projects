#a script that randomly selects 3 usernames for an AMA session
import random
interviewed = []
def quarantined_devs(names):
    get_names()
    interviewed_folks()
    uninterviewed_folks()

def get_names():
    for name in name_file:
        name = name.rstrip('\n')
        names.append(name)

def interviewed_folks():
    while len(interviewed) < len(names):
        to_be_interviewed = random.sample(names, 3)
        for i in to_be_interviewed: 
            interviewed.append(i)
            interviewed.append('Ifihan Olusheye')
            interviewed.append('Kromate')
            interviewed.append('LordGhostX')
            interviewed.append('Olalekan Kolapo')
            interviewed.append('Bello Gbadebo')

        interviewed_set = []
        for i in interviewed:
            if i not in interviewed_set:
                interviewed_set.append(i)
        print('INTERVIEWED FOLKS')
        print(interviewed_set)

def uninterviewed_folks():
    not_interviewed = []
    for i in names:
        if i not in interviewed:
            not_interviewed.append(i)
    print('UNINTERVIEWED FOLKS')        
    print(not_interviewed)
    
name_file = open(r"C:\Users\User\Desktop\python-projects\python_projects\quarantined-devs\dev-names.csv", "r")
names = []

quarantined_devs(names)
