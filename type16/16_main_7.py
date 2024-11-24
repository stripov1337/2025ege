
def sum(n):
    Flag=True
    while n!=0:
        a=n%10
        if a%2!=0:
            Flag=False
        n=n//10   
    return Flag


print(sum(43))
print(sum(44))

