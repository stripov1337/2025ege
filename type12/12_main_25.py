for x in range (3,10000):
    st = "5" + "2"*x
    while "72" in st or "522" in st or "2222" in st:
        if "72" in st: 
            st = st.replace("72","2",1)
        if "522" in st: 
            st = st.replace("522","27",1)
        if "2222" in st:
            st = st.replace("2222", "5",1)
    if (st.count("5")*5 + st.count("2")*2 + st.count("7")*7) == 63:
        print(x)
        break 