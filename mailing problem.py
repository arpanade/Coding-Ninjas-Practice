'''
keyword='zyxwvutsrqponmlkjihgfedcba'
s='zayb'


keyword='abcdefghijklmnopqrstuvwxyz'
s='abc'


keyword='qwertyuiopasdfghjklzxcvbnm'
s='perry'
'''


def timeTakenToMail(keyboard: str, s: str) -> int:


    #count=0
    count = abs(keyboard.index(s[0]))
    for i in range(len(s)-1):
        count=count+(abs(keyboard.index(s[i])-keyboard.index(s[i+1])))    # abs used to give positive integer even if it - 


    return count


keyboard='qwertyuiopasdfghjklzxcvbnm'
s='perry'

v=timeTakenToMail(keyboard,s)
print(v)


