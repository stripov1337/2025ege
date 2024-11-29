from itertools import * 
count_=0
for x in product("УЛЕЙ",repeat=4):
    word = ''.join(x)
    if word[0]!='Й' and word.count("У")==1 and word.count("Л")==1 and word.count("Е")==1 and word.count("Й")==1:
        count_+=1
print(count_)        