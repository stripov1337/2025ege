def frec(x,t):
    if x==t:
        return 1
    if x>t:
        return 0
    return frec(x+1,t) + frec(x+10,t)

print(frec(15,28))