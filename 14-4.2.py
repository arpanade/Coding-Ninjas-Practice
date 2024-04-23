from os import *
from sys import *
from collections import *
from math import *

def validAbbreviation (str, abbr):
	count=len(str)
	counter0=0
	li2=[]
	li=[]
	no= ""
	ite=0

	for ind in range(len(abbr)):
		if ord(abbr[ind])>47 and ord(abbr[ind])<58:
			no= abbr[ind]
			if (ind-1)!=-1:
				if ord(abbr[ind-1])>47 and ord(abbr[ind-1])<58:
					no=abbr[ind-1]+abbr[ind]
					li2[len(li2)-1]=int(no)
					continue
				else:
					li2.append(int(no))
			else:
				li2.append(int(no))
		else:
			li2.append(abbr[ind])
	for i in str:
		li.append(i)
	
	for i in li2:
		if isinstance(i,int):
			ite+=i
		else:
			if li[ite]==i:
				ite=ite+1
				continue
			else:
				return 'NO'
				break
	

	if count ==ite:
		return 'YES'
	else:
		return 'NO' 



str='race'
abbr='r2e'

u=validAbbreviation(str,abbr)

print(u)