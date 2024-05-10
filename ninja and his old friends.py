#friends=[3,2,1,4]
friends=[2,4]
n=len(friends)
k=4

for i in range(n):
    if friends[i]==k:
        k=k*2


print(k)