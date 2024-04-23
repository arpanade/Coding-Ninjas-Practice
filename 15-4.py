from os import *
from sys import *
from collections import *
from math import *

from typing import *

def sortOddEven(nums : List[int]):
    li2=[]
    li3=[]
    li4=[]


    for i in nums:
        if i%2==0 or i==0:
            li2.append(i)
        else:
            li3.append(i)
            
    l=len(li2)
    l2=len(li3)

    for f in range(l2):
        for g in range(0,l2-f-1):
            if li3[g]<li3[g+1]:
                li3[g], li3[g+1]= li3[g+1], li3[g]


    for k in range(l):
        for j in range(0,l-k-1):

            if li2[j]>li2[j+1]:
                li2[j], li2[j+1]= li2[j+1],li2[j]

   
    #x=li3+li2
    #return x

    for s in li3:
        li4.append(s)
    
    for t in li2:
        li4.append(t)

    
    return li4


nums=[9,6,2,4]

p=sortOddEven(nums)
print(p)