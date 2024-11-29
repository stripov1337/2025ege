from itertools import * 
a = []

for x in product("АИОУЭ",repeat=4):
    x = "".join(x)
    a.append(x)
print(a.index('ИААЭ')+1)