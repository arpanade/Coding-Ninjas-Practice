points=[[1,2,5],[3,1,1],[3,3,3]]
n=len(points)
score=[]

for i in range(n):
    count=points[i][0]
    for j in range(n-1):
        if count<points[i][j+1]:

            count=points[i][j+1]
        else:
            continue


    score.append(count)

#print(score)

count2=0

for y in score:
    count2=count2+y

print(count2)


