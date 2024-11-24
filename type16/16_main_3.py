def f(a):
    if a==1:
        return 1
    if a%2==0:
        return 2*f(a-1)
    if a%2!=0:
        return 5*a+f(a-2)

print(f(64))