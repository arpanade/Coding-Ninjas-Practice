row=int(input())
cols=2
arr=[]
for i in range(row):
    col=[]
    for j in range(2):
        col.append(int(input()))

    arr.append(col)   

print(arr)