#turbulent hills
#height=[1,2,10,3,5,1,10,10]
height=[9,4,2,10,7,8,8,1,9]
n=len(height)
li2=[]
for i in range(1,n-1):
    #print(height[i])
    if height[i-1]<height[i]> height[i+1]:
        li2.append(height[i-1])
        li2.append(height[i])
        li2.append(height[i+1])
print(li2)
