'''
a=[0,1,7,8]


if a[0]==0:
    a.pop(a[0])


print(a)

a=1
b=2
c=3

x=c*1
y=b*10
z=a*100

v=x+y+z
print(v)
'''
a=[0,1,3,4]

if a[0]==0:
    a.pop(a[0])

l=len(a)

inc=1
x=0
for i in range(l-1,-1,-1):
    
    inc=inc*10

    #print(inc*i)
    x=x+(inc*a[i])
    #print(inc)

#a.pop(a[l])
x=x//10
print(x)

