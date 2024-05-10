from os import *
from sys import *
from collections import *
from math import *

def solve(arr, k):

    li2=[]
    n=len(arr[0])

    for i in range(n):
        temp=[]
        for j in range(n):
            tot=(j+k)%n
            temp.append(arr[i][tot])
        li2.append(temp)
        
    arr.clear()
    for k in range(n):
        temp2=[]
        for s in range(n):
            temp2.append(li2[k][s])
        arr.append(temp2)
    
    return arr

arr=[[1,2,3],[4,5,6],[7,8,9]]
k=2  # number of rotation 

v=solve(arr,k)
print(v)

'''


arr=[[1,2,3],[4,5,6],[7,8,9]]
k=2
li2=[]
li3=[]
n=len(arr[0])

for i in range(n):
    temp=[]
    for j in range(n):
        tot=(j+k)%n
        temp.append(arr[i][tot])
    li2.append(temp)

print(li2)


'''