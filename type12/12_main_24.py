for x in range(100):
    for y in range(100):
        for z in range(100):
            st = "0" + "1"*x + "2"*y + "3" *z
            while "01" in st or "02" in st or "03" in st:
                st = st.replace("01","2302",1)
                st = st.replace("02","10",1)
                st = st.replace("03", "201",1)
            if st.count("1") == 60 and st.count("2") == 22 and st.count("3") == 17:
                print(st, x)
                
