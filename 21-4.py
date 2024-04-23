a=[1,10,5,2,8,1]
cout=1

le=len(a)
 
for i in range(le):
    tot=cout
    if a[i]>tot:
        cout=a[i]
    else:
        continue



cout2=cout

for j in range(le):
    tot2=cout2
    if a[j]<tot2:
        cout2=a[j]
    else:
        continue



diff=cout2-cout
final=abs(diff)


if final%2==0:
    print("even")

else:
    print("odd")