def frec(x,t):
    if x==t:
        return 1
    if x>t:
        return 0
    return frec(x+1,t)+frec(int(str(x)+"1"),t)

print(frec(1,555))