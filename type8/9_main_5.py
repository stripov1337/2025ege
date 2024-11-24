from itertools import *
a = []
for x in product('ЕИКНУЧ', repeat=3):
    x = ''.join(x)
    a.append(x)
print(a.index("КЕЕ")+1)
