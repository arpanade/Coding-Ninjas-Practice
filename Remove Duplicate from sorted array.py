arr=[1,1,2,2,4,4,5]
n=len(arr)
arr2=[]
for i in arr:
    if i  not in arr2:
        arr2.append(i)

print(arr2)

'''
def removeDuplicates(arr,n):
    # Write your code here.
    
    arr2=[]

    for i in arr:
        if i not in arr2:
            arr2.append(i)

    x=len(arr2)
    
    return x
'''

