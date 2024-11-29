from itertools import * 
count=0
for x in product('ВЕСНА', repeat=3):
    word = "".join(x)
    if word.count('А') >= 1:
        count+=1
print(count)