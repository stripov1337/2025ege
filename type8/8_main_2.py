from itertools import *
a = []

for x in product("УОА",repeat=5):
    x ="".join(x)
    a.append(x)
print(a[110])