fin = open('9-170.csv')
count=0

for st in fin:
    data = list(map(int,st.split(",")))
    data = sorted(data)
    doubles=[]
    for i in range (len(data)):
        if data.count(data[i]) > 1:
            doubles.append(data[i])
    if len(doubles)==2 and (sum(data)-sum(doubles))/4 <= sum(doubles):
        count+=1
print(count)
