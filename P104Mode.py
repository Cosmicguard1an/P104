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
modeRange = {'50-60':0, '60-70':0,'70-80':0}

for height,occurence in data.items():
    if 50 < float(height) < 60:
        modeRange['50-60'] += occurence
    elif 60 < float(height) < 70:
        modeRange['60-70'] += occurence
    elif 70 < float(height) < 80:
        modeRange['70-80'] += occurence

mode_Range,mode_Occurence = 0,0

