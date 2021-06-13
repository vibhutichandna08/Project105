import csv
import math

with open('std.csv', newline='') as f:
    reader = csv.reader(f)
    file = list(reader)
    data = file[0]


def mean(data):
    num = len(data)
    total = 0
    for m in data:
        total += int(m)
        mean = total/num
    return mean


sqrtlist = []
for num in data:
    sqr1 = int(num)-mean(data)
    sqr = sqr1*sqr1
    sqrtlist.append(sqr)
sum = 0
for sqrt in sqrtlist:
    sum += sqrt
    result = sum/(len(data)-1)
    std = math.sqrt(result)
print(std)
