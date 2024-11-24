def f(n):
    if n>25:
        return n*n+4*n+3
    if n<=25 and n%3==0:
        return f(n+1)+2*f(n+4)
    if n<=25 and n%3!=0:
        return f(n+2)+3*f(n+5)

def sum(n):
    sum_=0
    while n!=0:
        a=n%10
        sum_+=a
        n=n//10   
    return sum_

count_=0

for x in range(1,1001):
    if sum(f(x))==24:
        count_+=1

print(count_)

    