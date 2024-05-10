'''
def XOR(x, y):
	return ((x | y) - (x & y))

x, y = 3, 5
print(XOR(x, y))

# This code is contributed by lokesh
'''
#arr=[2,5,6]
arr=[1,2,3,4]
arr=[5]
li2=[]
ll=len(arr)

for i in range(ll-1):
    for j in range(i+1,ll):
        #tot=arr[i]+arr[j]
        tot=((arr[i]|arr[j])-(arr[i]&arr[j]))
        #print(tot)
        li2.append(tot)


print(li2)


big=li2[0]
ll2=len(li2)
if ll<=2:
    print(li2[0])
else:


    for k in range(0,ll2-1):

        if big>li2[k+1]:
            big=big
        else:
            big=li2[k+1]

    print(big)