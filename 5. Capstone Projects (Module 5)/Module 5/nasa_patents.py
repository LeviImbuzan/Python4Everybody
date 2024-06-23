import sqlite3

conn = sqlite3.connect('nasa_patents_db.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Center;
DROP TABLE IF EXISTS Status;
DROP TABLE IF EXISTS CaseNumber;
DROP TABLE IF EXISTS PatentNumber;
DROP TABLE IF EXISTS ApplicationSN;
DROP TABLE IF EXISTS Title;
DROP TABLE IF EXISTS PatentExpirationDate;
DROP TABLE IF EXISTS Full;

CREATE TABLE Center (
    id  INTEGER PRIMARY KEY,
    name    TEXT UNIQUE
);                 

CREATE TABLE Status (
    id  INTEGER PRIMARY KEY,
    title    TEXT UNIQUE
);

CREATE TABLE CaseNumber (
    id  INTEGER PRIMARY KEY,
    number    TEXT UNIQUE
);

CREATE TABLE PatentNumber (
    id  INTEGER PRIMARY KEY,
    string    TEXT UNIQUE
);

CREATE TABLE ApplicationSN (
    id  INTEGER PRIMARY KEY,
    serial    TEXT UNIQUE
);

CREATE TABLE Title (
    id  INTEGER PRIMARY KEY,
    description    TEXT UNIQUE
);

CREATE TABLE PatentExpirationDate (
    id  INTEGER PRIMARY KEY,
    date    TEXT UNIQUE
);

CREATE TABLE Full (
    id  INTEGER PRIMARY KEY,
    name_id  INTEGER, title_id INTEGER, number_id INTEGER, string_id INTEGER, serial_id INTEGER, 
    description_id INTEGER, date_id INTEGER
 
);
''')

# Open the CSV file with the correct encoding
with open('NASA_Patents.csv', 'r', encoding='utf-8') as handle:
    for line in handle:
        line = line.strip()
        pieces = line.split(',')
        if len(pieces) < 7:
            continue

        centers = pieces[0]
        statuss = pieces[1]
        case_numbers = pieces[2]
        patent_numbers = pieces[3]
        application_sns = pieces[4]
        titles = pieces[5]
        patent_experiation_dates = pieces[6]

        print(centers, statuss, case_numbers, patent_numbers, application_sns, titles, patent_experiation_dates)

        cur.execute('''INSERT OR IGNORE INTO Center (name) VALUES ( ? )''', (centers, ))
        cur.execute('SELECT id FROM Center WHERE name = ? ', (centers, ))
        name_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Status (title) VALUES ( ? )''', (statuss, ))
        cur.execute('SELECT id FROM Status WHERE title = ? ', (statuss, ))
        title_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO CaseNumber (number) VALUES ( ? )''', (case_numbers, ))
        cur.execute('SELECT id FROM CaseNumber WHERE number = ? ', (case_numbers, ))
        number_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO PatentNumber (string) VALUES ( ? )''', (patent_numbers, ))
        cur.execute('SELECT id FROM PatentNumber WHERE string = ? ', (patent_numbers, ))
        string_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO ApplicationSN (serial) VALUES ( ? )''', (application_sns, ))
        cur.execute('SELECT id FROM ApplicationSN WHERE serial = ? ', (application_sns, ))
        serial_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Title (description) VALUES ( ? )''', (titles, ))
        cur.execute('SELECT id FROM Title WHERE description = ? ', (titles, ))
        description_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO PatentExpirationDate (date) VALUES ( ? )''', (patent_experiation_dates, ))
        cur.execute('SELECT id FROM PatentExpirationDate WHERE date = ? ', (patent_experiation_dates, ))
        date_id = cur.fetchone()[0]

        cur.execute('''INSERT OR REPLACE INTO Full
            (name_id, title_id, number_id, string_id, serial_id, description_id, date_id)
            VALUES ( ?, ?, ?, ?, ?, ?, ?)''', 
            (name_id, title_id, number_id, string_id, serial_id, description_id, date_id))

        conn.commit()

conn.close()
