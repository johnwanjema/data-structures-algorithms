
def binarysearch(arr, target):
    start = 0
    end = len(arr) - 1
    asc = arr[-1] > arr[0]
    
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            if(asc):
                end = mid - 1
            else:
                start = mid + 1
        else:
            if(asc):
                start = mid + 1
            else:
                end = mid - 1
    
    return -1

asc = [12,33,45,56,67,78,80,90]
desc = [100,90,89,76,56,40,30,30,2,1]

print(binarysearch(asc,12))
print(binarysearch(desc,100))