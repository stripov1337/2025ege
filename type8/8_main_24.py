from itertools import *
a = []
for x in product("АВГЕН",repeat=4):
    x = ''.join(x)
    a.append(x)
print(a.index("ВВВВ")+1)