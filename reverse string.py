string="arpan"
#string='d4'
li2=[]


#print(string[1])

ll=len(string)

for i in range(ll-1,-1, -1):
    li2.append(string[i])

result=''.join(li2)

print(result)