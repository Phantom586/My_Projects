# import the Database Class from MyDatabase
from MyDatabase import Database

# Creating the instance of the Database Class
db = Database('records_bank')

def createdb():
    # Creating the Database and acquiring the cursor from the Connection Object
    db.create_db()

def createtable():
    # Creating the Table
    db.create_table('account_details', 'account_no integer', 'pin integer')

def insertValue():
    # Now Inserting Some Values
    db.insert_into_db('account_details', 123456, 3456)
    db.insert_into_db('account_details', 234556, 5667)

def query():
    # Querying the Values from the Database
    values = db.select_from_db('account_details')
    for value in values:
        print(value)

def update():
    # # Dictionary of the Values to be Updated.
    dict = {'pin':1234}

    db.update_db('account_details', dict, account_no=123456)

def remove():
    db.remove_from_db('account_details', account_no=123457, pin=3456)
    # db.remove_from_db('account_details', account_no=234556, pin=5667)

createdb()
# createtable()
# insertValue()
remove()
query()