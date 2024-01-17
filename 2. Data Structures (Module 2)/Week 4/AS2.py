fname = open ('mbox-short.txt')
count = 0
for line in fname:
    line = line.rstrip()
    if not line.startswith ('From ') : continue
    count = count + 1
    words = line.split()
    print (words[1])
print ('There were', count, 'lines in the file with From as the first word')