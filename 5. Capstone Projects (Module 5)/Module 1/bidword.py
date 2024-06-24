import sqlite3
import string

# Connect to the provided SQLite file
conn = sqlite3.connect('bidlistdb.sqlite')
cur = conn.cursor()

# Fetch descriptions from the database
cur.execute('SELECT id, description FROM CapsuleDescription')
description  = dict()
for message_row in cur:
    description [message_row[0]] = message_row[1]

# Fetch description _ids from the Messages table
cur.execute('SELECT description_id FROM Full')
counts = dict()
for message_row in cur:
    text = description [message_row[0]]
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.translate(str.maketrans('', '', '1234567890'))
    text = text.strip()
    text = text.lower()
    words = text.split()
    for word in words:
        if len(word) < 4:
            continue
        counts[word] = counts.get(word, 0) + 1

x = sorted(counts, key=counts.get, reverse=True)
highest = None
lowest = None
for k in x[:100]:
    if highest is None or highest < counts[k]:
        highest = counts[k]
    if lowest is None or lowest > counts[k]:
        lowest = counts[k]
print('Range of counts:', highest, lowest)

# Spread the font sizes across 20-100 based on the count
bigsize = 80
smallsize = 20

with open('bidword.js', 'w') as fhand:
    fhand.write("bidword = [")
    first = True
    for k in x[:100]:
        if not first:
            fhand.write(",\n")
        first = False
        size = counts[k]
        size = (size - lowest) / float(highest - lowest)
        size = int((size * bigsize) + smallsize)
        fhand.write("{text: '" + k + "', size: " + str(size) + "}")
    fhand.write("\n];\n")

print("Output written to bidword.js")
print("Open bidword.htm in a browser to see the visualization")
