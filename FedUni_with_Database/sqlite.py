import sqlite3

conn = sqlite3.connect('records.db')

c = conn.cursor()

# c.execute("""CREATE TABLE bankdb (
#     account_no integer,
#     pin integer
#     )""")

acc, pin = map(int, input('Enter the Account and pin').split())

# c.execute('INSERT INTO bankdb VALUES (123456, 3456)')
# c.execute('INSERT INTO bankdb VALUES (789456,2326)')
# c.execute('INSERT INTO bankdb VALUES (123434, 0896)')
# c.execute('INSERT INTO bankdb VALUES (657567, 8797)')
# c.execute('INSERT INTO bankdb VALUES (:account_no, :pin)', {'account_no':acc, 'pin':pin})


c.execute(f'SELECT * FROM bankdb where account_no={acc} and pin={pin}')

# c.execute(f'SELECT * FROM bankdb')

# print(c.fetchall())

if c.fetchone():
    print("The User Exists!!!")

conn.commit()

conn.close()