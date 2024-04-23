queue= [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


a=[]
b=[]

half=int(len(queue)//yy2)



for i in range(0,len(queue)):
    if i<half:
        a.append(queue[i])
    else:
        b.append(queue[i])

queue.clear()


for j in range(0,half):
    queue.append(a[j])
    queue.append(b[j])


print(queue)