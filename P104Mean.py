import csv

with open('HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
newData = []

for i in range(len(fileData)):
    num = fileData[i][2]
    newData.append(float(num))
    print(newData)

#mean
n = len(newData)
total = 0
for x in newData:
    total +=x

mean = total/n
print('The mean is '+str(mean))





