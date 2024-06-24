import sqlite3
import csv

conn = sqlite3.connect('bidlistdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Skill;
DROP TABLE IF EXISTS Grade;
DROP TABLE IF EXISTS Bureau;
DROP TABLE IF EXISTS Organization;
DROP TABLE IF EXISTS PostCity;
DROP TABLE IF EXISTS PostCountry;
DROP TABLE IF EXISTS TourofDuty;
DROP TABLE IF EXISTS Languages;
DROP TABLE IF EXISTS PostDifferential;
DROP TABLE IF EXISTS TED;
DROP TABLE IF EXISTS Incumbent;
DROP TABLE IF EXISTS CapsuleDescription;
DROP TABLE IF EXISTS Full;

CREATE TABLE Skill (
    id  INTEGER PRIMARY KEY,
    skill    TEXT UNIQUE
);                 

CREATE TABLE Grade (
    id  INTEGER PRIMARY KEY,
    grade    TEXT UNIQUE
);

CREATE TABLE Bureau (
    id  INTEGER PRIMARY KEY,
    name    TEXT UNIQUE
);

CREATE TABLE Organization (
    id  INTEGER PRIMARY KEY,
    title    TEXT UNIQUE
);

CREATE TABLE PostCity (
    id  INTEGER PRIMARY KEY,
    location    TEXT UNIQUE
);

CREATE TABLE PostCountry (
    id  INTEGER PRIMARY KEY,
    alias    TEXT UNIQUE
);

CREATE TABLE TourofDuty (
    id  INTEGER PRIMARY KEY,
    length    TEXT UNIQUE
);

CREATE TABLE Languages (
    id  INTEGER PRIMARY KEY,
    spoken    TEXT UNIQUE
);

CREATE TABLE PostDifferential (
    id  INTEGER PRIMARY KEY,
    percent   TEXT UNIQUE
);

CREATE TABLE TED (
    id  INTEGER PRIMARY KEY,
    date   TEXT UNIQUE
);

CREATE TABLE Incumbent (
    id  INTEGER PRIMARY KEY,
    person    TEXT UNIQUE
);

CREATE TABLE CapsuleDescription (
    id  INTEGER PRIMARY KEY,
    description    TEXT UNIQUE
);

CREATE TABLE Full (
    id  INTEGER PRIMARY KEY,
    skill_id  INTEGER, grade_id INTEGER, name_id INTEGER, title_id INTEGER, location_id INTEGER, 
    alias_id INTEGER, length_id INTEGER, spoken_id INTEGER, percent_id INTEGER, date_id INTEGER,
    person_id INTEGER, description_id INTEGER
);
''')

# Open the CSV file with the correct encoding
with open('2025BidList.csv', 'r', encoding='utf-8') as handle:
    csv_reader = csv.reader(handle)
    next(csv_reader)  # Skip the header row if there is one

    for row in csv_reader:
        if len(row) < 12:
            continue

        skills, grades, bureaus, organizations, post_citys, post_countrys, tour_of_dutys, languagess, post_differentials, teds, incumbents, capsule_descriptions = row

        cur.execute('''INSERT OR IGNORE INTO Skill (skill) VALUES ( ? )''', (skills, ))
        cur.execute('SELECT id FROM Skill WHERE skill = ? ', (skills, ))
        skill_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Grade (grade) VALUES ( ? )''', (grades, ))
        cur.execute('SELECT id FROM Grade WHERE grade = ? ', (grades, ))
        grade_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Bureau (name) VALUES ( ? )''', (bureaus, ))
        cur.execute('SELECT id FROM Bureau WHERE name = ? ', (bureaus, ))
        name_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Organization (title) VALUES ( ? )''', (organizations, ))
        cur.execute('SELECT id FROM Organization WHERE title = ? ', (organizations, ))
        title_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO PostCity (location) VALUES ( ? )''', (post_citys, ))
        cur.execute('SELECT id FROM PostCity WHERE location = ? ', (post_citys, ))
        location_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO PostCountry (alias) VALUES ( ? )''', (post_countrys, ))
        cur.execute('SELECT id FROM PostCountry WHERE alias = ? ', (post_countrys, ))
        alias_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO TourofDuty (length) VALUES ( ? )''', (tour_of_dutys, ))
        cur.execute('SELECT id FROM TourofDuty WHERE length = ? ', (tour_of_dutys, ))
        length_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Languages (spoken) VALUES ( ? )''', (languagess, ))
        cur.execute('SELECT id FROM Languages WHERE spoken = ? ', (languagess, ))
        spoken_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO PostDifferential (percent) VALUES ( ? )''', (post_differentials, ))
        cur.execute('SELECT id FROM PostDifferential WHERE percent = ? ', (post_differentials, ))
        percent_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO TED (date) VALUES ( ? )''', (teds, ))
        cur.execute('SELECT id FROM TED WHERE date = ? ', (teds, ))
        date_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Incumbent (person) VALUES ( ? )''', (incumbents, ))
        cur.execute('SELECT id FROM Incumbent WHERE person = ? ', (incumbents, ))
        person_id = cur.fetchone()[0]
      
        cur.execute('''INSERT OR IGNORE INTO CapsuleDescription (description) VALUES ( ? )''', (capsule_descriptions, ))
        cur.execute('SELECT id FROM CapsuleDescription WHERE description = ? ', (capsule_descriptions, ))
        description_id = cur.fetchone()[0]

        cur.execute('''INSERT OR REPLACE INTO Full
            (skill_id, grade_id, name_id, title_id, location_id, alias_id, length_id, spoken_id, 
            percent_id, date_id, person_id, description_id) 
            VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )''', 
            (skill_id, grade_id, name_id, title_id, location_id, alias_id, length_id, spoken_id, 
            percent_id, date_id, person_id, description_id)) 

        conn.commit()

conn.close()
