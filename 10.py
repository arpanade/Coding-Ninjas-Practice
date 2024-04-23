from sys import *
from collections import *
from math import *

from typing import *

def completeSum(a: List[int], n: int)-> List[int]:
    x=0
    li2=[]
    for i in range(0,n):
        x=a[i]+x

        li2.append(x)


    z=1
    t=0
    for j in range(n-1,-1,-1):
        z=z*10
        x=li2[j]*z
        t=t+x
    
    total=int(t/10)
    return total

a=[3,1,2]
n=len(a)
f=completeSum(a,n)
print(f)