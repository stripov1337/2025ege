def frec(x,t):
    if x==t:
        return 1
    if x<t or x==13:
        return 0
    return frec(x-1,t)+frec(x-2,t)+frec(x//3,t)
print(frec(19,6)*frec(6,4))