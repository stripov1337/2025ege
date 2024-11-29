from itertools import * 
count_=0
for x in product("01234567",repeat=5):
    word = "".join(x)
    if word[1] not in '01357' and word[-1] not in "26" and word.count("7")<=2:
        count_+=1
print(count_)