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

    #for i in head:
    #    if i==-1:
    #        head.pop()

    
    l=len(head)
    add=0

    for i in range(0,l):
        add=add+head[i]
        if head[i]==0:

            
            li2.append(add)
            add=0
            dest=i
            
        
        if head[i]==-1:
            #print(i)
            for u in range(dest,l):
                if head[u]==-1:
                    continue
                else:
                    if head[u]==0:
                        continue
                    else:
                        li2.append(head[u])
                #print(head[u])
            break
    
    return li2
    

#g=[0,6,0,4,5,-1]
g=[2,5,7,0,3,4,0,-1]
#g=[1,2,3,0,-1]
v=replaceWithSum(g)

print(v)