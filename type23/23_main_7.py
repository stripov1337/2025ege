def frec(x,t,c):
    if x==t and c==7:
        return 1
    if x>t:
        return 0
    return frec(x+1,t,c+1)+frec(x+2,t,c+1)+frec(x+3,t,c+1)

print(frec(3,22,0))