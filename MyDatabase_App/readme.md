# MyDatabase App
This is a Tkinter Python Application that Uses sqlite3 as Database to store Information Provided by the User.

![FedUni](images/sc1.png "MyDatabase_App")

## Modules :
### 1. Register :
With this Module you can register new users to the Database, just by providing his **Firstname**, **Lastnmae**, **User-Id**, **Password**, **Email**.

While Registering a User there are some things you need to consider :
1. **Email** should always be in the form of *abc@example.com*.
2. **Password** 
      a. First character should be *Capital*.
      b. It should contain atleast one *Special Characters(!@#$%^&*())* and *Digits(0-9)*.
 
 **Regular Expressions** are Used in order to make sure that these requirements are met and if not, proper error messages have been provided to notify it to the User.
 
**Note :** *User-Id* and *Password* is **Unique** for every user in the Database. 

### 2. SignIn :
With this Module you can Login to the Individual Users Account, just by entering his **User-Id** and **Password**.From where you'll be able to Update, Delete his/her details/Account from the Database.

### 3. Search :
With this Module You can Search for any User that is present in the Database.

### 4. Clear :
This Module is Used to Clear all the Inputs on the Window.

![FedUni](images/sc2.png "MyDatabase_App")

## Modules :
### 1. Update :
With this Module you can easily update you **User_FirstName**, **User_LastName** or **User_Email** by clicking on the **LOCKED** Button and Entering the Password For the User(For Verification) and Entering the Values You wish to Change and then *press the **UPDATE** Button*.

### 2. ShowDB :
With this Module you can view all the entries present in the Database.

### 3. Logout :
With this Module you can Logout of you Account and return back to the Main Screen of the App.



-------------------------------------------------------------------------------------------------------------------------------------------
**Thanks for Visiting my Repository**.
