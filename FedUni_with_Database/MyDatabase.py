import sqlite3

### This is a Database Class For making sqlite Database Operations smoother, just import the class in your
### Python File and it's ready to rock n' roll.
### Created by Ph@ntom586.

class Database:
    
    """
        Parameters:
            db_name = The name of the Database you want to create.

        Description:
            Accepts the name of the Databse you want to create.
    """
    
    def __init__(self, db_name):

        self.db_name = db_name
        # variables for the connection and the cursor objects
        self.conn = ''
        self.c = ''
    

    def create_db(self):
        
        """
        Description:
            Creates the Database and a cursor to execute sqlite queries.
        """
        
        # Creating the connection Object.
        self.conn = sqlite3.connect(f'{self.db_name}.db')
        
        # Getting a cursor from the connection.
        self.c = self.conn.cursor()

        print(f"DATABASE CREATED ---> {self.db_name}")


    def create_table(self, table_name, *fields):

        """
        Parameters:
            table_name = The name of the table you want to create.

            fields = The fields along with their Type whic needs to be added to the Table.
                     Ex :('firstname text', 'salary integer')

        Description:
            To Create Table in the Database along with specific fields.
        """

        q = f" CREATE TABLE {table_name} ("

        if fields:
            for field in fields:
                q += f'{field}, '
            # removing the extra ',' from the query.
            q = q[:len(q)-2]
            # adding ')' at the end of the query to complete the query.
            q += ' )'
        else:
            print("Creating the Table without any Fields!!!")

        # Context Manager for the Connection object
        with self.conn:
            # Executing the Query
            self.c.execute(q)
        
        # Making COMMIT to the DATABASE
        self.conn.commit()

        print(f"TABLE Created ---> {table_name}")


    def select_from_db(self, table_name, select_what=None, **kwargs):
        
        """
        Parameters:
            select_what = what do you want to select form a particular table.

            table_name = the name of the table from which you want to select from.
            
            **kwargs = any number of 'name=values' to pass to the query.

        Description:
            To Select anything from the Database.
        """

        if select_what != None:
            q = f"SELECT {select_what} FROM {table_name} "
        else:
            q = f"SELECT * FROM {table_name} "
        if kwargs:
            q += "WHERE "
            for key in kwargs:
                q += f"{key}={kwargs[key]} AND "
            # to remove the extra 'and' from the query
            q = q[:len(q)-4]

        # Executing the Query
        self.c.execute(q)

        print("VALUES FETCHED!!!")
        # Fetching the Results and returning to the user.
        return self.c.fetchall()


    def insert_into_db(self, table_name, *values):

        """
        Parameters:
            table_name = the name of the table from which you want to select from.

            *values(required) = all the values you want to insert into the database

        Description:
            To Insert values into the Database.
        """

        if values:
            q = f"INSERT INTO {table_name} VALUES{values}"
        else:
            print("INSERT requires some values to be passed to the Table.")

        # Context manager for the Connecion object
        with self.conn:
            self.c.execute(q)

        # Making COMMIT to the Database
        self.conn.commit()

        print(f"INSERTED INTO ---> {table_name}")


    # def update_db(self, table_name, **set_values, **kwargs):

    #     """
    #     Parameters:
    #         table_name = the name of the table from which you want to select from.

    #         **set_values = the values you want to set(update) in the table.

    #         **kwargs = parameters to match the specific field you want to make the update to. 

    #     Description:
    #         Updates the fields of the provided table.
    #     """

    #     # Flag to indicate whether to execute the query or not. 
    #     flag = True

    #     q = f"UPDATE {table_name} SET "

    #     if set_values:
    #         for key in set_values:
    #             q += f'{key}={set_values[key]} AND '
    #         # removing the extra 'AND' from the query.
    #         q = q[:len(q)-4]
    #     else:
    #         flag = False
    #         print("Update Failed!! Please pass the Values to Update in the Table.")

    #     if kwargs:
    #         q += "WHERE "
    #         for key in kwargs:
    #             q += f'{key}={kwargs[key]} AND '
    #         # removing the extra 'AND' from the query.
    #         q = q[:len(q)-4]
    #     else:
    #         flag = False
    #         print("Update Failed!! Please pass the Correct Matching Parameters.")

    #     # Checking If everything is Alright. 
    #     if flag == True:
    #         # Context Manager for the Connection object.
    #         with self.conn:
    #             self.c.execute(q)

    #     # Making COMMIT to the Database.
    #     self.conn.commit()

    #     print(f"UPDATED TABLE ---> {table_name}")
        

    def remove_from_db(self, table_name, **kwargs):

        """
        Parameters:
            table_name = the name of the table from which you want to select from.

            **kwargs = Field values of the Entry(row) you want to DELETE from the Table.

        Description:
            To DELETE a specific Entry(row) from the Table.
        """

        # Flag to indicate whether to execute the query or not.
        flag = True

        q = f'DELETE FROM {table_name} WHERE '
        
        if kwargs:
            for key in kwargs:
                q += f'{key}={kwargs[key]} AND'
            # removing the extra 'AND' from the query.
            q = q[:len(q)-4]
        else:
            flag = False
            print("DELETE Failed!!! Please Enter [valid] values of the Entry(row) you want to Delete.")

        if flag == True:
            # Context Manager for the Connection object.
            with self.conn:
                self.c.execute(q)
        
        # Making COMMIT to the Database
        self.conn.commit()

        print(f"DELETED Entry from the TABLE ---> {table_name}")