from itertools import *
count_=0
for x in product("012345678",repeat=5):
    word = "".join(x)
    if word.count("0")==1 and word.count("10")==0 and word.count("01")==0 and word.count("30")==0\
        and word.count("03")==0 and word.count("50")==0 and word.count("05")==0 and word.count("70")==0 and word.count("07")==0 and word[0]!="0":
        count_+=1
print(count_)