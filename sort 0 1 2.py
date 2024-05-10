arr=[0,1,2,1,2,1,2,1]
n=len(arr)

zero=0
one=0
two=0


li2=[]

for i in arr:
    if i==0:
        zero=zero+1

    if i==1:
        one=one+1

    if i==2:
        two=two+1

arr.clear()

print(zero)
i=0

while i<zero:
    li2.append(0)
    i=i+1

j=0

while j<one:
    li2.append(1)
    j=j+1

k=0

while k<two:
    li2.append(2)
    k=k+1


print(li2)
    


