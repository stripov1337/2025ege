st = ">" + "2"*15 + "3"*40 + "1" *20  + "<"

while not "><" in st:
    st = st.replace(">1","3>",1)
    st = st.replace(">2","2>",1)
    st = st.replace(">3","1>",1)
    st = st.replace("3<","<1",1)
    st = st.replace("2<","<3",1)
    st = st.replace("1<","<2",1)
print(st)
print(st.count("1") + st.count("2")*2 + st.count("3")*3)