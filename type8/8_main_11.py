from itertools import * 
count_=0
for x in product("ВЕРТНО", repeat=8):
    word = "".join(x)
    if word.count("Е")==3 and word.count("О")==1 and word.count("Р")==1 and word.count("В")==1 and word.count("Т")==1 \
        and word.count("Н")==1 and word.count("ОО")==0 and word.count("ЕО")==0 and word.count("ОЕ")==0 \
             and word.count("ЕЕ")==0 and word.count("ВВ")==0 and word.count("ВР")==0 and word.count("ВТ")==0 and word.count("ВН")==0 \
                and word.count("РВ")==0 and word.count("РР")==0 and word.count("РТ")==0 and word.count("РН")==0 and word.count("ТТ")==0 \
                    and word.count("ТВ")==0 and word.count("ТР")==0 and word.count("ТН")==0 and word.count("НВ")==0 and word.count("НР")==0 \
                        and word.count("НТ")==0 and word.count("НН")==0:
                        count_+=1
print(count_)
