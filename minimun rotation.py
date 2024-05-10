'''
s='ninja'
s='cccccc'
x=list(s)
n=len(x)
#print(x)

#string= ''.join(x) 
x=list(s)
for i in range(n):
    x.append(x[0])
    x.pop(0)
    string="".join(x)
    if string==s:
        print(i+1)
        break
    else:
        string=""

'''
def minimumRotations(n,s):
    
    x=list(s)
    for i in range(n):
        x.append(x[0])
        x.pop(0)
        string="".join(x)
        if string==s:
            count=i+1
            return count
            break
        else:
            string=""


s='cccccc'
x=list(s)
n=len(x)

v=minimumRotations(n,s)
print(v)