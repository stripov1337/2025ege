
for x in range(2,11):
    n=364
    st=""
    base=x
    while n>0:
        digit=n%base
        st=str(digit)+st
        n=n//base
    print(st,base)

