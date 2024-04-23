'''
def addOneToNumber(arr):
    if arr[0]==0:
        arr.pop(0)


    l=len(arr)
    x=0
    inc=1
    li2=[]

    for i in range(l-1,-1,-1):
        inc=inc*10


        x=x+(inc*arr[i])
        
    
    x=x//10+1
    li2.append(x)


    




    return li2
   ''' 

from os import *
from sys import *
from collections import *
from math import *

def addOneToNumber(arr):

    if arr[0]==0:
        arr.pop(arr[0])
    li3=[]
    li2=[]
    l=len(arr)
    x=0
    inc=1

    for i in range(l-1,-1,-1):
        inc=inc*10


        x=x+(inc*arr[i])
    
    x=x//10+(1)

    li2.append(x)

    li2=str(li2[0])
    #print(type(li2))
    for i in li2:
        li3.append(int(i))
        
    return li3



f=[0,1,2,3,5]
o=addOneToNumber(f)
print(o)