def frec(x,t):
    if t==x:
        return 1
    if x>t:
        return 0
    return frec(x+1,t)+frec(x+2,t)+frec(x+(x+1),t)
print(frec(2,10))