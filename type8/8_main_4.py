from itertools import * 
a = []
for x in product("АКРУ",repeat=5):
    x = "".join(x)
    a.append(x)
print((a.index("УКАРА")-a.index("РУКАА"))+1)