from itertools import*
count_=0
for x in product("ГЕОРИЙ",repeat=7):
    word = ''.join(x)
    if word.count("Г")==2 and word.count("Е")==1 and word.count("О")==1 and word.count("Р")==1 and word.count("И")==1 and word.count("Й")==1\
         and word.count("ГГ")==0 and word.count("ЕЕ")==0 and word.count("ОО")==0 and word.count("РР")==0 and word.count("ИИ")==0 and word.count("ЙЙ")==0:
         count_+=1
print(count_)