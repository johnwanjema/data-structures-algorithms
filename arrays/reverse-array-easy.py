mylist = [1,2,3,45,5,353]

def swap(mylist, index1, index2):
    temp =  mylist[index1]
    mylist[index1] = mylist[index2]
    mylist[index2] = temp
     
def reverse(mylist):
    start= 0
    end = len(mylist) - 1

    while start < end:
        swap(mylist, start,end)
        start += 1
        end -= 1
    
    for x in mylist:
        print(x)
    
print(reverse(mylist))