
def lastname(name1, name2):
    arg1 = name1.split( ' ')
    arg2 = name2.split(' ')
    if arg1[1] != arg2[1]: #if the second part of the split name is not equal to the args2,
        return arg1[1] < arg2[1] #return arg1 as lesser than arg2
    else: #if last names[1] are same, sort by first name
        return arg1[0] < arg2[0]

def firstname(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    #to sort by the first names
    if arg1[0] != arg2[0]:
        return arg1[0] < arg2[0]
    else: 
        return arg1[1] < arg2[1]

def merge(left, right, compare):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def mergesort(names, compare = lambda x,y: x < y):
    if len(names) < 2:
        return names[:]
    else:
        middle = len(names) // 2
        left = mergesort(names[:middle], compare)
        right = mergesort(names[middle:], compare)
        return merge(left, right, compare)
names = ['Pop Lee', 'Shu Rin', 'Er Lin']
newnames = mergesort(names, lastname)
print('sorted by last names', newnames)
firsts = mergesort(names, firstname)
print('sorted by first names', firsts)
