from os import *
from sys import *
from collections import *
from math import *

def maximumDifferece(n, arr):
    # Write your code here.
    cout=1

    for i in range(n):
        tot=cout
        if arr[i]>tot:
            cout=arr[i]
        else:
            continue

    
    cout2=cout

    for j in range(n):
        tot2=cout2
        if arr[j]<tot2:
            cout2=arr[j]
        else:
            continue

    
    diff=cout2-cout

    final=abs(diff)

    if final%2==0:
        return 'EVEN'
    else:
        return 'ODD'


a=[1,10,5,2,8,1]
#a=[2,9,3,4]
le=len(a)

v=maximumDifferece(le,a)
print(v)