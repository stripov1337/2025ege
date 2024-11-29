from itertools import * 
count_=0
for x in product("012345678",repeat=5):
    word = "".join(x)
    if word[0] not in "01357" and word[-1] not in "18" and word.count("3")<=1:
        count_+=1
print(count_)