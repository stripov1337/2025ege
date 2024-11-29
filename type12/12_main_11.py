print(int("222",8))

number = 8
base=3
st=''
while number>0:
    digit=number%base
    st=str(digit)+st
    number=number//base
print(st)