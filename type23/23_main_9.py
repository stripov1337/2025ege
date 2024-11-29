def frec(x,t):
    if x==t:
        return 1
    if x>t or str(x).count("5")>0:
        return 0
    return frec(x+1,t)+frec(x+5,t)
print(frec(1,30))