from itertools import *
a=[]
for x in product('ПОРТ',repeat=5):
    x = ''.join(x)
    a.append(x)
print((a.index('ТОПОР'))-(a.index("РОПОТ"))+1)
