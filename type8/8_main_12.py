from itertools import *
count_=0
for x in product("012345678",repeat=6):
    word = "".join(x)
    if word[1] not in "`01357" and word[-1] not in "23" and word.count('1')>=2:
        count_+=1
print(count_)