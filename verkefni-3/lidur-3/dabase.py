import sqlite3 as sql

with sql.connect("users.db") as db:
  cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
uID INTEGER PRIMARY KEY,
uName VARCHAR(20) NOT NULL,
fName VARCHAR(20),
lName VARCHAR(20),
passWd VARCHAR(20) NOT NULL);
''')

cursor.execute('''
INSERT INTO user(uName, fName, lName, passWd)
VALUES("test_user", "Bobby", "Fisher", "bobby_fister")
''')
db.commit()

cursor.execute("SELECT * FROM user")
print(cursor.fetchall())
