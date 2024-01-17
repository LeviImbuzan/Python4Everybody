import re

fname = open('regex_sum_1651094.txt')
x=list()

for line in fname:
    line =line.rstrip()
    y = re.findall('([0-9]+)' , line)
    x = x+y

sum=0
for z in x:
    sum = sum + int(z)

print(sum)