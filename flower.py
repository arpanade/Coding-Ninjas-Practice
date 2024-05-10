
def flower(n,p):
#p=[1,2,3,17,18,10,12]

    l=len(p)
    count=0
    for i in range(0,l-1):
        if p[i+1]!=i+2:
            count=count+1

    return count


n=int(input())
p=[]
for i in range(n):
    p.append(int(input()))

v=flower(n,p)
print(v)