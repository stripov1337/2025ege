from itertools import *
a = []

for x in product('АГИЛМОРТ',repeat=4):
    x = "".join(x)
    a.append(x)
print(a.index('ТТАЛ')+1)