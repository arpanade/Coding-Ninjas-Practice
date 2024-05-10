
def square(n,m):
    tot=0
    for i in range(n):
        tot=(n*m)+tot
        n=n-1
        m=m-1

    #print(tot)
    return tot

n=3
m=5
v=square(n,m)
print(v)



