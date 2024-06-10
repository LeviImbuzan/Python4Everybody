import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('email_database.db')
cur = conn.cursor()

# Drop the Counts table if it exists
cur.execute('DROP TABLE IF EXISTS Counts')

# Create the Counts table
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)
''')

# Prompt the user for a file name, with a default option
fname = input('Enter file name: ')
if len(fname) < 1: 
    fname = 'mbox-short.txt'

# Open the file
fh = open(fname)
for line in fh:
    # Look for lines that start with 'From: '
    if not line.startswith('From: '): 
        continue
    pieces = line.split()
    email = pieces[1]
    # Extract the domain name
    org = email.split('@')[1]
    # Check if the domain name is already in the database
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        # Insert new domain name with a count of 1
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        # Update the count for the existing domain name
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    # Commit the transaction
    conn.commit()

# Retrieve and print the top 10 domain names by count
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# Close the cursor and the connection
cur.close()
fh.close()
conn.close()