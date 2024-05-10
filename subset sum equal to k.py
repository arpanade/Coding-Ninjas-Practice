#arr=[1,2,3,4]

def subsetSumToK(n, k, arr):

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    flag = False

    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == k or arr[i] + arr[j] == k:
                flag = True
                break


    if flag==True:
        x="true"
        return x
    elif flag==False:
        y="false"
        return y



#arr=[1,7,2,9,10]
arr=[6,1,2,1]
n=len(arr)

k=6

v=subsetSumToK(n,k,arr)

print(v)








'''
flag = False

for i in range(n):
    for j in range(i+1, n):
        if arr[i] == k or arr[i] + arr[j] == k:
            flag = True
            break

if flag==True:
    x="true"
    print(x)
elif flag==False:
    y="false"
    print(y)
'''