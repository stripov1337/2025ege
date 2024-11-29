x = int("120",7)-int('60',8)
number = x
base = 6
st=''
while number>0:
    digit = number%base
    st=str(digit)+st
    number=number//base
print(st)