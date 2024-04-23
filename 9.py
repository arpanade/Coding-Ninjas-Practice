





li=[1,2,3,4]

n=len(li)



z=1
t=0
for i in range(n-1,-1,-1):
    z=z*10
    x=li[i]*z
    print(x)
    t=t+x

total=int(t/10)
print(total)

