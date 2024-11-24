count=0
fin = open("9-194.csv")

for st in fin:
    data = list(map(int,st.split(",")))
    data = sorted(data)
    doubles =[]
    chet=[]
    nechet=[]
    for i in range(len(data)):
        if data.count(data[i])>1:
            doubles.append(data[i])
        if data[i]%2==0:
            chet.append(data[i])
        if data[i]%2!=0:
            nechet.append(data[i])
    if len(doubles)==0 and len(chet)>len(nechet) and sum(nechet)>sum(chet):
        count+=1
print(count)
    