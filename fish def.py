def fishEater(fishes):
    li2=[]
    for i in range(0,len(fishes)-1):
        if i==0:
            max=fishes[0]
            li2.append(fishes[0])
        
        if fishes[i]=max:
            max=fishes[i]
            li2.append(max)
    
    return li2



#fish=[4,2,1,6]

fish=[4,4,2,4]

v=fishEater(fish)

print(v)

'''
def fishEater(fishes):
    li2=[]
    max_size = fishes[0]
    li2.append(max_size)
    
    for size in fishes[1:]:
        if size > max_size:  # Change '>= to '>'
            max_size = size
            li2.append(max_size)
    
    return li2

fish = [4, 4, 2, 4]
v = fishEater(fish)
print(v)
