for x in range(91,200):
    st = "1" * x
    while "111" in st:
        st = st.replace("111","2",1)
        st = st.replace("2222","333",1)
        st = st.replace("33","1",1)
    print(x, st.count("1"))

