count=0
fin = open('9-170.csv')

for st in fin:
    data = list(map(int,st.split(',')))
    data = sorted(data)
    doubles=[]
    for i in range (len(data)):
        if data.count(data[i]) > 1:
            doubles.append(data[i])
    if len(doubles)==3 and (sum(data)-sum(doubles))*3 <= doubles[0]*doubles[1]*doubles[2]:
        count+=1
print(count)
