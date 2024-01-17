fname = open ('mbox-short.txt')
counts = dict()
for line in fname:
    if line.startswith ('From: '):
        line = line.rstrip().split()
        word = line[1]
        counts[word] = counts.get(word,0) + 1
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print (bigword, bigcount)