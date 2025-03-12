arr=[1,2,3,4,56]

def linearsearch(arr , target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

result=linearsearch(arr , 4)
if result !=-1:
    print (result)
else:
    print("not found")

