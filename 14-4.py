'''
strr="hello"
abbr="1e2o"

strr=[*strr]
abbr=[*abbr]
'''
strr=['h','e','l','l','o']
abbr=['1','e','2','o']



for i in range(0,len(abbr)):
    print(i)
    x=abbr[i]
    try:
        k=int(x)
    except:
        k=str(x)
    if type(k)==int:
        i=i+k
    if abbr[i]==strr[i]:
        print("matched")

        
    
            
            


            
        

        




