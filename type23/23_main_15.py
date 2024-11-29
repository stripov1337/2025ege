def frec(x,t):
    if x==t:
        return 1
    if x>t or x==14:
        return 0
    return frec(x+1,t)+frec(x+2,t)+frec(x*3,t)

print(frec(1,10)*frec(10,15))