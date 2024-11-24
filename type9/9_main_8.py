count=0
fin = open("9-191.csv")

for st in fin: 
    data = list(map(int,st.split(",")))
    data = sorted(data)
    doubles=[]
    ndoubles=[]
    for i in range (len(data)):
        if data.count(data[i]) > 1:
            doubles.append(data[i])
        else:
            ndoubles.append(data[i])
   
    if len(doubles)>=1 and len(ndoubles)>=1 and sum(ndoubles)/len(ndoubles)>sum(doubles)/len(doubles):
        count+=1
print(count)
