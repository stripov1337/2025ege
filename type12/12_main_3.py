max = 0
for x in range(3,10000):
    st = "1" + "2" * x
    while "12" in st or "322" in st or "222" in st:
        if "12" in st:
            st = st.replace("12","2",1)
        if "322" in st:
            st = st.replace("322", "21", 1)
        if "222" in st:
            st = st.replace("222", "3", 1)
    if (st.count("1")*1+st.count("2")*2+st.count("3")*3) > max:
        max = st.count("1")*1+st.count("2")*2+st.count("3")*3
print(max)