st = "1" + "2" * 51

while "12" in st or "1" in st:
    if "12" in st:
        st = st.replace("12","2221",1)
    else: 
        st = st.replace("1", "222222",1)
print(st)
print(st.count("2"))
