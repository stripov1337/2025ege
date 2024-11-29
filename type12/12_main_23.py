for x in range(100,500):
    st = "1" * x
    while "333" in st or "111" in st:
        st = st.replace("333","11",1)
        st = st.replace("111","3",1)
    print(x,st)