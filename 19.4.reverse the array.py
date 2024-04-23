arr=[1,2,3,4,5,6]

m=3
l=len(arr)
li2=[]

for i in range(-1,-m,-1):
    #print(arr[i])
    li2.append(arr[i])

for j in range(-1,-m,-1):
    #print(arr[i])
    arr.pop(arr[i])

#print(arr)
#print(li2)

for k in li2:
    arr.append(k)

print(arr)