from itertools import *
a=[]
for x in product("АОУ",repeat=5):
    word = "".join(x)
    a.append(word)
print(a[:10],sep='\n')
print(a[124])