n = 4**2015+8**2016-2**2017-150
base=2
st=''
while n>0:
    digit=n%base
    st=str(digit)+st
    n=n//base
print(st.count("0"))