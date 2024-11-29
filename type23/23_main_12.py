def frec(x,t):
    if x==t:
        return 1
    if x>t or x==35:
        return 0
    return frec(x+1,t) + frec(x*3,t) + frec(x*4,t)

print(frec(2,8)*frec(8,70))