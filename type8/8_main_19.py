from itertools import *
count_=0
for x in product("0123456789ABCDE",repeat=5):
    word = "".join(x)
    if word.count("8")==1 and word.count("A")+word.count("B")+word.count("C")+word.count("D")+word.count("E")>=2 and word[0] not in "0":
        count_+=1
print(count_)