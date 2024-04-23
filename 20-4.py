
def isKthBitSet(n: int, k: int) -> bool:

    li2=[]
    x=bin(n)[2:]

    l=len(x)
    for i in range(l):
        li2.append(int(x[i]))

    
    #print(li2)

    if li2[l-k]==1:
        return True
    else:
        return False



n=3
k=2

v=isKthBitSet(n,k)

print(v)























'''
li2=[]
x=bin(n)[2:]

l=len(x)

for i in range(l):
    li2.append(int(x[i]))


print(li2)

if li2[l-k]==1:
    print("YES")
else:
    print("NO")

    '''