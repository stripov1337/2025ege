import sys
sys.setrecursionlimit(4500)


def frec(x,t):
    if x==t:
        return 1
    if x<t:
        return 0 
    if x>4:
        return frec(x-1,t)+frec(x-3,t)+frec(x%4,t)
    return frec(x-1,t)+frec(x-3,t)

print(frec(22,2))