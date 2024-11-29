from itertools import *
a=[]
for x in product('АОУ',repeat=5):
    x = ''.join(x)
    a.append(x)
print(a.index('УАУАУ')+1)