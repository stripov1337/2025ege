def f(n):
    if n<=15:
        return n*n+3*n+9
    if n>15 and n%3==0:
        return f(n-1)+n-2
    if n>15 and n%3!=0:
        return f(n-2)+n+2


def sum(n):
    Flag=True
    while n!=0:
        a=n%10
        if a%2!=0:
            Flag=False
        n=n//10   
    return Flag

count_=0

for x in range(1,1001):
    if sum(f(x))==True:
        count_+=1


print(count_)