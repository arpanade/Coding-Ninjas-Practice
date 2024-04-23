
def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here

    a=m**(1/n)
    b=int(a)
    print(a)
    if b==a:
        return b
    else:
        return -1


x=NthRoot(1953125,9)
print(x)









'''

def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here

    a=m**(1/n)
    return a

x=NthRoot(1953125,9)
print(x)
'''