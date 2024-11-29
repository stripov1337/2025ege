from itertools import * 
count_=0
for x in product('ЗЕРКАЛО',repeat=6):
    word = "".join(x)
    if word.count("К")<=4 and word.count("З")<=1 and word.count("Е")<=1 and word.count("Р")<=1 and word.count("А")<=1 and word.count("Л")<=1 and word.count("О")<=1 and word.count("К")>0:
        count_+=1
print(count_) 