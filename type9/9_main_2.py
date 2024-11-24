count = 0

fin = open("9-160.csv")

for st in fin:
    data = list(map(int,st.split(',')))
    data = sorted(data)
    if data[-1] < sum(data[:-1]) and data[0] + data[-1] == data[1] + data[-2]:
        count+=1
print(count)

