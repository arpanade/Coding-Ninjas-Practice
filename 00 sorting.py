arr=[2,1,2,4,1,2,1,0,4,4,3,3]

#arr=[6,0,3,5]

n=len(arr)


yo=0


for j in range(0,n):
    for i in range(0,n-1):
        if arr[i]>=arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        
    

print(arr)