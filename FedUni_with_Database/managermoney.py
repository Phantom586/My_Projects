class MoneyManager():

       
    def __init__(self):
        '''Constructor to set username to '', pin_number to an empty string,
           balance to 0.0, and transaction_list to an empty list.'''


        
    def add_entry(self, amount, entry_type):
        '''Function to add and entry an amount to the tool. Raises an
           exception if it receives a value for amount that cannot be cast to float. Raises an exception
           if the entry_type is not valid - i.e. not food, rent, bills, entertainment or other'''


    def deposit_funds(self, amount):
        '''Function to deposit an amount to the user balance. Raises an
           exception if it receives a value that cannot be cast to float. '''


        
    def get_transaction_string(self):
        '''Function to create and return a string of the transaction list. Each transaction
           consists of two lines - either the word "Deposit" or the entry type - food etc - on
           the first line, and then the amount deposited or entry amount on the next line.'''


    def save_to_file(self):
        '''Function to overwrite the user text file with the current user
           details. user number, pin number, and balance (in that
           precise order) are the first four lines - there are then two lines
           per transaction as outlined in the above 'get_transaction_string'
           function.'''


        



        