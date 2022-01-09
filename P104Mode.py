import csv
from collections import Counter

with open('HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
newData = []

for i in range(len(fileData)):
    num = fileData[i][2]
    newData.append(float(num))

#mode
data = Counter(newData)
modeRange = {'100-120':0, '120-140':0,'140-160':0}

for weight,occurence in data.items():
    if 50 < float(weight) < 60:
        modeRange['50-60'] += occurence
    elif 60 < float(weight) < 70:
        modeRange['60-70'] += occurence
    elif 70 < float(weight) < 80:
        modeRange['70-80'] += occurence

mode_Range,mode_Occurence = 0,0

