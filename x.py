from os import *
from sys import *
from collections import *
from math import *

def doorStatus(n):

    a=[0]*n
    for i in range(1,n+1):
        for j in range(i,n+1,i):
            #a[j-1]^=1
            if a[j-1]==0:
                a[j-1]=1
            else:
                a[j-1]=0
    result=''.join(map(str,a))
    return result


print(doorStatus(10))