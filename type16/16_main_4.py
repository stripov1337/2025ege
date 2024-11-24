def f(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return 3*f(a-1)+2*f(a-2)

print(f(6))