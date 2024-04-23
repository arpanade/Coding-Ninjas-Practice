from os import *
from sys import *
from collections import *
from math import *

def findAllSelfDivdingNumbers(lower, upper):

    inp=[]
    for m in range(lower, upper):
        inp.append(m)

    li2=[]
    li3=[]

    for t in range(0,len(inp)):
        st=str(inp[t])
        for i in st:
            li2.append(int(i))

        l=len(li2)

        count=0

        for j in li2:
            if j==0:
                break
            if inp[t]%j==0:
                count=count+1

        if count==l:
            li3.append(inp[t])
        
        li2.clear()

    return li3
    
x=findAllSelfDivdingNumbers(15,45)

print(x)