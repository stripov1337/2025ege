from itertools import * 
count_=0
words=[]
for x in product('АБВГ',repeat=5):
    word = "".join(x)
    if word.count("Г") == 1 and word[-1]=="Г" or word.count("Г") == 0:
        count_+=1
print(count_)