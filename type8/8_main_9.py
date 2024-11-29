from itertools import *
count_=0
for x in product("КАПН",repeat=6):
    word = "".join(x)
    if word.count("КК")==0 and word.count("АА")==0 and word.count("Н")==1 and word.count("П")==1 and word.count("К")==2 and word.count("А")==2:
        count_+=1
print(count_)