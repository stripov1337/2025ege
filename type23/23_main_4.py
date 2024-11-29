def frec(x,t):
    if x==t:
        return 1
    if x<t:
        return 0
    return frec(x-1,t)+frec(x//2,t)
print(frec(30,12)*frec(12,1))