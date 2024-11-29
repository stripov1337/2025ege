num = 8**1341-4**1342+2**1343-1344
base = 2
st=''
while num>0:
    digit=num%base
    st=str(digit)+st
    num=num//base
print(st.count("1"))