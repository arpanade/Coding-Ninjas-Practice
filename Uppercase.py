str="my name is kachori"
result=""

for i in range(len(str)):
    
    if i==0 or str[i-1]==" ":
        x=str[i].upper()
        result=result+x

    else:
        result=result+str[i]

print(result)