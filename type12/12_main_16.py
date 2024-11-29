n=81**2017+9**5223-81
b=9
st=''
while n>0:
    digit=n%b
    st=str(digit)+st
    n=n//b
print(st.count("8"))