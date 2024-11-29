print(int("121",6))

number = 6
base =3 
st=""
while number>0:
    digit = number%base
    st=str(digit)+st
    number=number//base
print(st)