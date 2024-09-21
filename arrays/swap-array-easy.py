mylist = [1,2,3,45,5,353]

def swap(mylist, index1, index2):
    temp =  mylist[index1]
    mylist[index1] = mylist[index2]
    mylist[index2] = temp
     
print(swap(mylist,0,3))