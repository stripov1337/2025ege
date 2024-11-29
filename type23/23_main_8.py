# source=image (1).webp

def frec(x,t,c):
    if x==t:
        return 1
    if x>t:
        return 0 
    if c==1:
        return frec(x*2,t,2)+frec(x*3,t,2)
    if c==2:
        return frec(x+1,t,1)+frec(x+3,t,1)
    if c==0:
        return frec(x*2,t,2)+frec(x*3,t,2)+frec(x+1,t,1)+frec(x+3,t,1)

print(frec(1,9999,0))