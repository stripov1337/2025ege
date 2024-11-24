fin = open("9-168.csv")
count = 0

for st in fin:
    data=list(map(int,st.split(',')))
    data = sorted(data)
    countp=0
    for i in range(len(data)):
        if data[i] > sum(data)/len(data):
            countp+=1
    if countp >= 3:
        count+=1
print(count)