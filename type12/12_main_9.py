for x in range(2,11):
    base=x
    num=432
    st=""
    while num>0:
        dig=num%base
        st=str(dig)+st
        num=num//base
    print(st,base)

