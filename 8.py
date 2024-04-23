from sys import *
from collections import *
from math import *

from typing import *

def completeSum(a: List, n: int)-> List[int]:
    x=0
    result=[]
    for i in range(0,n):
        x=a[i]+x
        #print(x)
        #result.append(x)
        print(x,end=" ")
        
    return result
     

c=[1,2,3]
v=3
h=completeSum(c,v)
#print(h)










'''
from typing import List

def completeSum(a: List[int], n: int) -> List[int]:
    x = 0
    result = []
    for i in range(n):
        x += a[i]
        result.append(x)
    return result

c = [1, 2, 3]
v = 3
h = completeSum(c, v)
print(h)
'''