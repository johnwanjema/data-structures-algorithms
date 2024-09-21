mylist = [1,2,3,45,5,353]

def linearSearch(list,key):
    for x in list:
        if x == key:
            return True
    return False

    # Second option
    return key in list
    
print(linearSearch(mylist))