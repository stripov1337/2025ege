from itertools import *
a =[]
for x in product('АВГДИНОР',repeat=4):
    x="".join(x)
    a.append(x)
print(a.index('ГОАА')+1)