# source=image.webp
def frec(x,t,c):
    if x==t and c==6:
        return 1
    if x>t:
        return 0

    return frec(x+1,t,c+1)+frec(x+2,t,c+1)+frec(x*2,t,c+1)

print(frec(1,20,0))