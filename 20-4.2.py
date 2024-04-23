from os import *
from sys import *
from collections import *
from math import *

"""
List Node Class
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None
    def __del__(self):
        if(self.next):
            del self.next

"""
def replaceWithSum(head):

    li2=[]
    if head[0]==0:
        head.pop(0)

    for i in head:
        if i==-1:
            head.pop()

    
    l=len(head)
    add=0

    for i in head:
        add=add+i
        if i==0:
            li2.append(add)
            add=0

    return li2


g=[0,6,0,4,5,0,-1]
v=replaceWithSum(g)

print(v)

