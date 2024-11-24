
def f(a):
    if a==1:
        return 1
    if a>1:
        return 2*f(a-1)+g(a-1)-2
        
def g(a):
    if a==1:
        return 1
    if a>1:
        return f(a-1)+2*g(a-1)


print(f(14)+g(14))