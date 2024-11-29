def frec(x,t):
    if x==t:
        return 1
    if x>t or x==15:
        return 0
    return frec(x+1,t)+frec(x+3,t)+frec(x+(x-1),t)
print(frec(2,10)*frec(10,20))