
n=4
k=2

#li=set('sonu')

li=["sonu","somi","kiki","keka"]

li1=[]
li2=[]
'''
for i in range(0,n):
    x=str(input())
    li.add(x)
'''


l=len(li)
print(l)
print(li)
for i in li:
    print(i[0])

    for j in li:
        if i[j]==i:
            li1.append(i[j])
        else:
            li2.append([j])