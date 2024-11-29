from itertools import * 
count_=0
for x in product("КАЛИЙ",repeat=5):
    word = "".join(x)
    if word[0]!= "Й" and word.count("К")==1 and word.count("А")==1 and word.count("Л")==1 and word.count("И")==1 and word.count("Й")==1 and word.count("ИАК")==0:
        count_+=1
print(count_)