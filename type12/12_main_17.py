n=3*289**2024+81*49**121-9*16**81-6011
b=31
count_=0
while n>0:
    dig=n%b
    if dig <=17:
        count_=count_+dig
    n=n//b
print(count_)