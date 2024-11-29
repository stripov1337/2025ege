max = 0 
for x in range(3,1563):
    st = "1" + "2"*x
    while "12" in st or "322" in st or "222" in st:
        if "12" in st: 
            st = st.replace("12","2",1)
        if "322" in st: 
            st = st.replace("322","21",1)
        if "222" in st:
            st = st.replace("222","3",1)
    if len(st) > max:
        max = len(st)
print(max)