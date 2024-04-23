a=[5,5]
b=[1,2,3,4,5]

li2=[]

for i in b:
    print(i)
    for j in b:

        if i+j==a[1]:
            li2.append(j)
            li2.append(i)
        break




print(li2)