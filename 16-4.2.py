a=[3,4,5,-2,7]

for i in range(0,len(a)):
    if a[i]<0:
        count=i
        mi=a[i]

#print(min)
m=mi
min = abs(mi)

 


for j in range(count-1,-1,-1):

    if a[j]<min:
        a.pop(j)
    else:
        a.pop(m)
        break




print(a)