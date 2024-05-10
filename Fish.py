fish=[4,2,3,1,5]
fish=[4,4,2,4]

fish=[1,2,3,4]
li2=[]

n=len(fish)


max=fish[0]
li2.append(fish[0])


for i in range(1,n):
    if fish[i]>=max:
        max=fish[i]
        li2.append(max)

print(li2)





