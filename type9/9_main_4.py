fin = open("9-162.csv")
count=0

for st in fin:
    data = list(map(int,st.split(',')))
    data = sorted(data)
    if data[-1]**3 >= (data[0]*data[1]*data[2])*2 and data[0] > 10:
        count+=1
print(count)