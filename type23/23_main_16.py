t=30
x=21
def frec(x,t):
    if x==t:
        return 1
    if x > t:
        return 0
    return frec(x+1,t) + frec(x+2,t) + frec(x+4,t)

print(frec(21,30))