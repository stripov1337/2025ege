def f(n):
    if n <=3:
        return n
    if n>3 and n%2==0:
        return n+f(n-1)
    if n>3 and n%2!=0:
        return n*n+f(n-2)

count_=0

for x in range(3000):
    if f(x) < 10**8:
        count_+=1
print(count_)
