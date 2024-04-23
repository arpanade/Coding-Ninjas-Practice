mat=[[1, 2],[0, 5]]

l=len(mat[1])

list2=[]

for i in range(0,l):
    if i%2==0:
        for j in mat[i]:
            list2.append(j)
    else:
        for k in range(0,l):
            list2.append(mat[i][l-k-1])


print(list2)   
