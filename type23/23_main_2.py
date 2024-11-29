def frec(x,t):
    if x==t:
        return 1
    if x>t or x==10 or x==15:
        return 0
    return frec(x+1,t)+frec(x+2,t)+frec(x+3,t)

print(frec(5,11)*frec(11,18))