#a script that randomly selects 3 usernames for an AMA session
import random
interviewed = []
def quarantined_devs(names):
    get_names()
    interviewed_folks()
    uninterviewed_folks()

def get_names():
    for i in name_file:
        i = i.split()
        names.append(i)

def interviewed_folks():
    while len(interviewed) < len(names):
        to_be_interviewed = random.sample(names, 3)
        for i in to_be_interviewed: 
            interviewed.append(i)

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
    
name_file = open("C:/Users/User/Desktop/OMARRR/Codes/quarantined-devs/dev-names.csv", "r")
names = []

quarantined_devs(names)
