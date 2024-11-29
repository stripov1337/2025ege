from itertools import *
count_=0
for x in product('012345678',repeat=7):
    word="".join(x)
    if word[0] not in'037' and word.count("00")==0 and word.count("11")==0 and word.count("22")==0 and word.count("33")==0 and word.count("44")==0\
        and word.count("55")==0 \
            and word.count("66")==0 and word.count("77")==0 and word.count("88")==0:
                count_+=1
print(count_)