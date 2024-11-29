from itertools import *
a =[]
for x in product('ВЕКНО',repeat=5):
    x = ''.join(x)
    a.append(x)
print(a.index('ОНННЕ')+1)