def binary_search(lists,x):
    l=0
    r=len(arr)
    mid=0
    while l<=r:
        mid=(l+r)//2
        if arr[mid] < x:
            l=mid+1
        elif arr[mid] > x:
            r=mid-1
        else:
            return arr[mid]
    return -1
import random
arr = []
for i in range(1, 100):
    arr.append(random.randint(1, 100))  
print(arr)
count = len(arr)

for outer in range(count-1):
    for i in range(count-outer-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
print(arr)
x = int(input('enter number for binary search : '))
if binary_search(arr,x)==-1:
    print("Number is not found")
else:
    print("Number is found")