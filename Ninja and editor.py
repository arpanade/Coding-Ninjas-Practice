from os import *
from sys import *
from collections import *
from math import *

def editSentence(s):
    # Write your code here.
    li2=[]

    for i in range(len(s)):
        if i==0:

            if ord(s[i])>=65 and ord(s[i])<=90:
                x=ord(s[i])+32
                #li2.append(chr(" "))

                li2.append(chr(x))
            else:
                y=ord(s[i])
                li2.append(chr(y))
        else:
            
            if ord(s[i])>=65 and ord(s[i])<=90:
                x=ord(s[i])+32
                li2.append(chr(" "))
                li2.append(chr(x))
            else:
                y=ord(s[i])
                
                li2.append(chr(y))
    
    c="".join(li2)

    return c
            
            



d="ArpanAde"

v= editSentence(d)

print(v)

















'''
arr="CodingNinjasIsACodingPlatform"

a='az'
li2=[]

#65  #90  #97  #122

for i in range(len(arr)):

    if i==0:
        if ord(arr[i])>=65 and ord(arr[i])<=90:
            x=ord(arr[i])+32

            
            li2.append(chr(x))

        else:
            y=ord(arr[i])
            li2.append(chr(y))
    else:
        if ord(arr[i])>=65 and ord(arr[i])<=90:
            x=ord(arr[i])+32

            li2.append(" ")
            li2.append(chr(x))

        else:
            y=ord(arr[i])
            li2.append(chr(y))

c=''.join(li2)
print(c)

'''