for x in range(1,25):
    number = x
    base=4
    st=""
    while number > 0:
        digit = number % base
        st = str(digit)+st
        number = number//base
    print(st,x)