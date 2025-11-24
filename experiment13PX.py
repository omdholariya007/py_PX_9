f1 = open("python.txt",'r')
count = 0
lines = 0
words= 0
for i in f1.readlines():
    lines+=1
f1.seek(0)
lin = f1.read()
s=lin.split()
for i in s:
    for j in i:

        count+=1
    words+=1
print(words,count,lines)

#2
l1=[]
f2 = open("python.txt",'r')
for i  in f2:
    l1.append(i)
print(l1)
#3
import csv
file = open("data.csv",'r')
cread = csv.reader(file)
for row in cread:
    print(row)
