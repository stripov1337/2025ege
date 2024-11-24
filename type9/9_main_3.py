count = 0

fin = open("9-161.csv")
for st in fin:
    data = list(map(int,st.split(',')))
    data = sorted(data)
    doubles = []
    for i in range(len(data)):
        if data.count(data[i]) > 1:
            doubles.append(data[i])
    if data[-1] < sum(data[:-1]) and (data[0] == data[1] or data[1] == data[2] or data[2]==data[3]):
        count+=1
print(count)