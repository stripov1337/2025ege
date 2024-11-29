

def frec(x,t):
    if x==t:
        return 1
    if x>t or x==7 or x==21:
        return 0
    return frec(x+1,t)+frec(x*2,t)+frec(2*x+1,t)+frec(x*10,t)
print(frec(1,35)*frec(35,40)*frec(40,50))