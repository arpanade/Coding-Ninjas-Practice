
'''
def findDuplicate(arr):
    l=len(arr)
    li2=[]
    for i in arr:
        if i not in li2:
            li2.append(i)
        elif i in li2:
            return li2[0]
'''


def findDuplicate(arr):
    l=len(arr)
    li2=[]
    for i in arr:
        if i not in li2:
            li2.append(i)
        elif i in li2:
            return i

arr=[2,4,5,6,4,6]

v=findDuplicate(arr)
print(v)