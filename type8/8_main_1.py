from itertools import * 
count_=0
for x in product("0123456789ABCD",repeat=5):
    word = "".join(x)
    if word.count("9")==1 and word.count("A")+word.count("B")+word.count("C")+word.count("D")<=3 and word[-1] not in "0":
        count_+=1
print(count_)