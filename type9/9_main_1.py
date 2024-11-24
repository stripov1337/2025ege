fin = open("9-157.csv")
count = 0
for st in fin:
    data = list(map(int,st.split(",")))
    data = sorted(data)
    if data[0] == data[1] and data[2]==data[3] and data[4]==data[5]:
        count += 1
print(count)