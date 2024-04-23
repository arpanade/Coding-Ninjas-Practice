li=[1,9,8,4,5,5,5,5]

l=len(li)
x=int(l/3)
li2=[]

for i in range(0,l):
    for j in range(i+1,l):
        if li[i]==li[j]:
            li2.append(li[j])

print(li2)
'''
li = [1, 9, 8, 4, 5, 5, 5, 5]
li2 = []

for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if li[i] == li[j] and li[i] not in li2:
            count = li.count(li[i])
            for _ in range(count):
                li2.append(li[i])

print(li2)
'''