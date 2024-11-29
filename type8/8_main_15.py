from itertools import * 
count_=0
for x in product("01234567",repeat=5):
    word = "".join(x)
    if word.count("6")==1 and word.count("16")==0 and word.count("61")==0 and word.count("36")==0 and word.count("63")==0\
         and word.count("56")==0 and word.count("65")==0 and word.count("67")==0 and word.count("76")==0 and word[0]!="0":
         count_+=1
print(count_)