'''
you have eat
you have read
you are eat
you are read
we have eat
we have read
we are eat
we are read

'''


arr=[['you','we'],['have','are'],['eat', 'read']]





'''


arr=[['you','we'],['have','are'],['eat', 'read']]

ans=[]

#print(len(arr))

ll=len(arr)  #3
ll2=len(arr[0])

for i in range(ll2):
    for j in range(ll2):
        for k in range(ll2):
            tot=arr[0][i]+" "+arr[1][j]+" "+arr[2][k]
            ans.append(tot)
            print(tot)




#print(ans)

'''