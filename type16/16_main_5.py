def f(a):
    if a<=3:
        return a
    if a>3 and a%2==0:
        return 2*a+f(a-1)
    if a>3 and a%2!=0:
        return a*a+f(a-2)

count_=0


for x in range(1,101):
    if f(x)%3==0:
        count_+=1
print(count_)