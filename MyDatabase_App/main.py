import tkinter as tk
from tkinter import *

# importing tkinter as themed-tkinter module
import tkinter.ttk as ttk

from tkinter import messagebox, scrolledtext, PhotoImage

# importing my Custom-sqlite-Database File
from MyDatabase import Database

# Creating an instance of the Database Class
my_db = Database('records_bank')



win = tk.Tk()

# Setting the Window Size
win.geometry('390x580')
win.minsize(390, 580)
win.maxsize(390, 580)

# Configuring the Style for the themed-tkinter module
style = ttk.Style()

# Title for the Window
win.title("My Database App")


# ---------------------- Entry Widgets Variables -----------

fname_var = tk.StringVar()    # Variable for Firstname
lname_var = tk.StringVar()    # Variable for Lastname
uid_var = tk.StringVar()      # Variable for User-Id
uid = ''
pas_var = tk.StringVar()      # Variable for User-Password
pas = ''
email_var = tk.StringVar()    # Variable for User-Email
pinentry_var = tk.StringVar() # Variable for the Password-verify Button


# ---------------------- Buttons ---------------------------

preview_btn = ''          # Button for Preview Function
register_btn = ''         # Button for Register Function
signin_btn = ''           # Button for SignIn Function
search_btn = ''           # Button for Search Function
statusbtn_var = tk.StringVar() # Text Variable for status_btn
status = "LOCKED"

SUNKABLE_BUTTON = 'SunkableButton.TButton'  # Style for themed-tkiner module

# ----------------------- Path for Icons -------------------

lock_img = "icons/lock1.png"
unlock_img = "icons/unlock1.png"

# ----------------------- PhotoImage Object for the Button --

image = lock_img
img = PhotoImage(file=image)


# ----------------------- Functions -------------------------

def remove_all_widgets():

    """
    Description:
        Function to remove all the widgets from the window.
    """
    for widget in win.winfo_children():
        widget.grid_remove()


def clear_pin_entries(des):

    """
    Parameters :
        des = Check whic of the Pin Entries to be Cleared.

    Description:
        Function for Clearing Pin Entries on the Window.
    """
    global fname_var, lname_var, uid_var, pas_var, email_var

    if des == 'userpass':
        uid_var.set('')
        pas_var.set('')
    elif des == 'cred':
        fname_var.set('')
        lname_var.set('')
        email_var.set('')
    else:
        uid_var.set('')
        pas_var.set('')
        fname_var.set('')
        lname_var.set('')
        email_var.set('')

    
def create_table():

    """
    Description:
        Function for Creating Table in the Database. 
    """
    my_db.create_table('account_details',
                        'user_fname text',
                        'user_lname text',
                        'user_id text',
                        'user_pass text',
                        'user_email text')


def add_user(fname, lname, u_id, u_pass, email):

    """
    Parameters:
        fname = the 'First name' of the User to be Registered.
        lname = the 'Last name' of the User to be Registered.
        u_id = the 'Id' of the User to be Registered.
        u_pass = the 'Password' of the User to be Registered.
        email = the 'email' of the User to be Registered.
    
    Description:
        Function to Add a User to the Database.
    """
    global register_btn

    # To ensure whether the Records of the new user doesn't exist in the Database.
    flag = True

    # Just making Sure all the inputs are Valid.
    if fname == '' and lname == '' and u_id == '' and u_pass == '' and email == '':
        # Issuing the Roor Message if not.
        messagebox.showerror('Error!!', 'Blank Fields are not Allowed!!')
    else:
        # Retrieving the user_id and user_pass of all the Users and checking if the User exist already. 
        check = my_db.select_from_db('account_details', ['user_id', 'user_pass'])
        # print(check)
        for entries in check:
            # If user_id and user_pass is present already in the Database then issue a warning for that.
            if u_id and u_pass in entries:
                flag = False
                messagebox.showwarning('Field Error!!', "Please! Use Another Username and Password!!")
                # Clearing the Entries of User-Id and Password Fields.
                clear_pin_entries('userpass')
                break

        # Making Sure everything is alright.
        if flag:
            # Inserting the New User Details into the Database.
            my_db.insert_into_db('account_details',fname, lname, u_id, u_pass, email)
            # Clearing the Entries except the User-Id and Password Fields.
            clear_pin_entries('cred')
            # Issuing Process Successful Info.
            messagebox.showinfo('User Accounts', 'User has been Added Successfully!')


def validate_user(u_id, u_pass):

    """
    Parameters:
        u_id = the 'Id' of the User to be Vaidated.
        u_pass = the 'Password' of the User to be Validated.

    Description:
        Function to Validate if the User Exists or not.
    """

    global search_btn

    # Just making Sure all the inputs are Valid.
    if u_id != '' and u_pass != '':
        # Retrieving the Details of all the Users and checking if it exists.
        user = my_db.select_from_db('account_details', user_id=u_id, user_pass=u_pass)
        if user:
            print("User Exists!!!")
            remove_all_widgets()
            create_user_screen(user)
        else:
            # If User Doesn't Exists Issuing a Proper Warning.
            print("User Doesn't Exists!!!")
            # Clear all Entries.
            clear_pin_entries('')
            messagebox.showerror('Login Error!!', 'Sorry! The User doesn\'t Exists!')
    else:
        messagebox.showerror('Error!!', 'Blank Fields are not Allowed!!')
        

def query_db():

    """
    Description:
        Function to See the Contents of the Database and Debug Whenever necessary.
    """
    c = my_db.select_from_db('account_details') ## Retrieving all info from the Database.
    # c = my_db.select_from_db('account_details', user_id='1716410101') ## Retrieving For Specific user_id
    # c = my_db.select_from_db('account_details', ['user_id', 'user_pass']) ## Retrieving user_id and user_pass of all the users in the Database.
    # for values in c:
    #     print(values)
    print(c)


def preview(u_id, u_pass, msg=None):

    """
    Parameters:
        u_id = the 'Id' of the User to be Previewed.
        u_pass = the 'Password' of the User to be Previewed.
        msg = for custom messages.

    Description:
        Function to just make sure that all the Details filled by the User is Correct.
    """
    # Just making Sure all the inputs are Valid.
    if u_id != '' and u_pass != '':
        # Retrieving the Details of the User with User_id and User_pass.
        result = my_db.select_from_db('account_details', user_id=u_id, user_pass=u_pass)
        # print(result)
        # Passing the Values along with the message to be displayed in the Output Window.
        if msg:
            output_win(result, msg)
        else:
            output_win(result, "Preview Results : ")
    else:
        messagebox.showerror('Error!!', 'Blank Fields are not Allowed!!')


def search(u_fname, u_id):

    """
    Parameters:
        u_id = the 'Id' of the User to be Previewed.
        u_fname = the 'First Name' of the User to be Previewed.

    Description:
        Function to search whether the User exixts or not.
    """

    # Creating a list of the inputs in order to get desired output.
    lst = [['u_fname', u_fname], ['u_id', u_id]]

    # Checking which of the inputs are to be inserted in the Query
    lst = [i for i in lst if i[1] != '']

    # Checking if the list in not empty.
    if lst != []:
        # If the length of the list is 1 that means there is only one parameter in the list.
        if len(lst) == 1:
            if lst[0][1] == 'u_fname':
                result = my_db.select_from_db('account_details', user_fname=u_fname)
            else:
                result = my_db.select_from_db('account_details', user_id=u_id)
        else:
            # else there are both parameters inputed by the user.
            result = my_db.select_from_db('account_details', user_id=u_id, user_fname=u_fname)

    # Passing the Values along with the message to be displayed in the Output Window.
    output_win(result, "Search Results :")


def extract_info(user):
    """
    Parameters:
        u_id = the 'Id' of the User to be Previewed.
        u_pass = the 'Password' of the User to be Previewed.

    Description:
        to extract all different fields from the specific row of a table.
    """

    global fname_var, lname_var, uid_var, pas_var, email_var
    # print(user)
    user = list(user[0])
    # print(user)
    fname_var.set(user[0])
    lname_var.set(user[1])
    uid_var.set(user[2])
    pas_var.set(user[3])
    email_var.set(user[4])


def output_win(str, msg):

    """
    Parameters:
        str = the string of results to be printed.
        msg = the message to be printed.

    Description:
        Function to Display the Provided Values and Message in the Output Window.
    """

    text_widget_2 = tk.scrolledtext.ScrolledText(win, width=12, height=6)
    
    text_widget_2.insert('insert', f'-------- {msg} --------' + '\n')
    for text in str:
        for txt in text:
            text_widget_2.insert('insert', txt + '\n')
            text_widget_2.insert('insert', '-----------------------' + '\n')
    text_widget_2.grid(row=9, columnspan=2, padx=10, sticky="news")
    text_widget_2.config(state="disabled")


def shortcuts(param):

    """
    Parameters:
        param = the string for the shortcut to be performed.
    
    Description:
        Function to Handle the Shortcuts provided in the Window.
    """
    if param == "quit":
        win.destroy()


def pass_verify(u_pass):
    """
    Parameters:
        u_pass = the 'user_pass' of the user.

    Description:
        to verify if the user is Authentic or not.
    """

    global top, status, pinentry_var

    if status ==  "LOCKED":

        top = tk.Toplevel(win)
        top.title("Verify!!")

        style.configure(SUNKABLE_BUTTON, foreground='green')

        top.geometry('220x100')
        top.minsize(220, 100)
        top.maxsize(220, 100)

        lb1 = tk.Label(top, text="Enter the Password for the User :")
        lb1.grid(row=0, columnspan=4, padx=20, sticky="news")

        u_p = tk.Entry(top, textvariable=pinentry_var)
        u_p.config(show='*')
        u_p.grid(row=1, columnspan=4, padx=20, sticky="news", pady=10)

        u_p.focus_set()

        btn = ttk.Button(top, text="Verify", style=SUNKABLE_BUTTON)
        btn.bind("<Button-1>", lambda x: btn_status(u_p.get(), u_pass))
        btn.grid(row=2, column=1, columnspan=2, sticky="news", pady=10)

        top.mainloop()

    else:
        
        btn_status()



def btn_status(t_pass=None, u_pass=None):
    """
    Parameters:
        t_pass = the 'pass' entered by the user in verification process.
        u_pass = the 'user_pass' of the user to verify during state change.

    Description:
        to check whether the button is in LOCKED state or not.
    """
    global statusbtn_var, fname, lname, email, status, top, pinentry_var, img, status_btn

    # Checking if the Passwords Exixts or not.
    if t_pass and u_pass:
        if t_pass == u_pass:
            # If the Passwords Match then,
            
            # Create a PhotoImage Object to change the Icon of the Button.
            img = PhotoImage(file=unlock_img)
            # Setting that icon to the Button
            status_btn.config(image=img)
            # Clearing the Pin Entry.
            pinentry_var.set('')
            # Destroying the Pin Verification Window.
            top.destroy()
            # Changing the Buttons Text to UNLOCKED.
            statusbtn_var.set("UNLOCKED")
            # Making the Entries Editable.
            fname.config(state=NORMAL)
            lname.config(state=NORMAL)
            email.config(state=NORMAL)
            # Setting the Global Variable to UNLOCKED.
            status = "UNLOCKED"
        else:
            # if not then Display the Error Message and Clear the Pin Entry.
            messagebox.showerror('Authentication Error!!!', "Please Try Again!!")
            pinentry_var.set('')
    else:
        # If the Status is UNLOCKED then set the button's text to LOCKED.
        statusbtn_var.set("LOCKED")
        # Create a PhotoImage Object to change the Icon of the Button.
        img = PhotoImage(file=lock_img)
        # Setting that icon to the Button
        status_btn.config(image=img)
        # Making the Entries Non-Editable.
        fname.config(state=DISABLED)
        lname.config(state=DISABLED)
        email.config(state=DISABLED)
        status = "LOCKED"



# ---------------------- Key Shortcuts ------------------
win.bind("<Control-q>", lambda e:shortcuts("quit"))

# Always leave this method enabled as it creates a connection and cursor objects to work with the Database.
my_db.create_db()

# Methods Below can be enabled or disabled depending on their usage. 
# create_table()

# Method to Remove a Secific Entity from the Database.
# my_db.remove_from_db('account_details', False, user_id=1716410101, user_pass=1234)

# Method to Delete the Table form the Database.
# my_db.drop_table('account_details')

# query_db()



# --------------- User Interface Functions ----------------

def create_login_screen():

    """
    Description:
        Function to create the login screen.
    """

    global uid, pas

    # Text-Widgets for Displaying the Info and Results.
    text_widget = tk.scrolledtext.ScrolledText(win, width=12, height=6)     # Text-Widget Variable
    text_widget_1 = tk.scrolledtext.ScrolledText(win, width=12, height=6)   # Another Text-Widget Variable

    # The Title of the Window.
    lb1 = tk.Label(win, text="Database App")
    lb1.config(font=("Source Code Pro", 28))
    lb1.grid(row=0, columnspan=2, ipadx=60, ipady=20)

    # ------------- Form Labels and Inputs --------------

    lb2 = tk.Label(win, text="FIRSTNAME : ")
    lb2.config(font=("Source Code Pro", 10))
    lb2.grid(row=1, column=0, sticky="e")

    fname = tk.Entry(win, textvariable=fname_var)
    fname.grid(row=1, column=1, pady=2, ipadx=70, sticky="nws")

    fname.focus_set()

    lb3 = tk.Label(win, text="LASTNAME : ")
    lb3.config(font=("Source Code Pro", 10))
    lb3.grid(row=2, column=0, sticky="e")

    lname = tk.Entry(win, textvariable=lname_var)
    lname.grid(row=2, column=1, pady=2, ipadx=70, sticky="nws")

    lb4 = tk.Label(win, text="USER-ID : ")
    lb4.config(font=("Source Code Pro", 10))
    lb4.grid(row=3, column=0, sticky="e")

    uid = tk.Entry(win, textvariable=uid_var)
    uid.grid(row=3, column=1, pady=2, ipadx=70, sticky="nws")

    lb5 = tk.Label(win, text="PASSWORD : ")
    lb5.config(font=("Source Code Pro", 10))
    lb5.grid(row=4, column=0, sticky="e")

    pas = tk.Entry(win, textvariable=pas_var)
    pas.config(show="*")
    pas.grid(row=4, column=1, pady=2, ipadx=70, sticky="nws")

    lb6 = tk.Label(win, text="EMAIL : ")
    lb6.config(font=("Source Code Pro", 10))
    lb6.grid(row=5, column=0, sticky="e")

    email = tk.Entry(win, textvariable=email_var)
    email.grid(row=5, column=1, pady=2, ipadx=70, sticky="nws")

    # --------------------------------------------------------

    # ----------------- Information Text Block ---------------
    text_widget.insert('insert', """USER-ID and PASSWORD are unique for everyone!!\nFor SignIn Only USER-ID and PASSWORD Fields are required!!\nTo Search Somebody Input his USER-ID and PASSWORD.""")
    text_widget.grid(row=6, columnspan=2, padx=10, pady=20, sticky="news")
    text_widget.config(state="disabled")

    # ----------------- Buttons --------------------

    frame_btns = tk.Frame(win)
    frame_btns.grid(row=7, columnspan=3)

    style.configure(SUNKABLE_BUTTON, foreground='green')

    preview_btn = ttk.Button(frame_btns, text="Preview", style=SUNKABLE_BUTTON)
    preview_btn.bind("<Button-1>", lambda x: preview(uid.get(), pas.get(), '1'))
    preview_btn.grid(row=0, column=0)

    register_btn = ttk.Button(frame_btns, text="Register", style=SUNKABLE_BUTTON)
    register_btn.bind("<Button-1>", lambda x: add_user(fname.get(), lname.get(), uid.get(), pas.get(), email.get()))
    register_btn.grid(row=0, column=1)

    signin_btn = ttk.Button(frame_btns, text="SignIn", style=SUNKABLE_BUTTON)
    signin_btn.bind("<Button-1>", lambda x: validate_user(uid.get(), pas.get()))
    signin_btn.grid(row=0, column=2)

    search_btn = ttk.Button(frame_btns, text="Search", style=SUNKABLE_BUTTON)
    search_btn.bind("<Button-1>", lambda x: search(fname.get(), uid.get()))
    search_btn.grid(row=0, column=3)

    clear_btn = ttk.Button(frame_btns, text="Clear", style=SUNKABLE_BUTTON)
    clear_btn.bind("<Button-1>", lambda x: clear_pin_entries(''))
    clear_btn.grid(row=0, column=4)

    # --------------- The Output Text Block -----------------------

    lb7 = Label(win, text="OUTPUT : ")
    lb7.grid(row=8, columnspan=2, pady=20)

    text_widget_1.insert('insert', """This is Output Window""")
    text_widget_1.grid(row=9, columnspan=2, padx=10, sticky="news")
    text_widget_1.config(state="disabled")

    # Some Helpful Information.

    lb8 = Label(win, text="Press 'Ctrl+q' to Quit the App.")
    lb8.grid(row=10, columnspan=2, pady=20)


def create_user_screen(user):

    """
    Parameters:
        user = details of the user whose account is being accessed.
    Description:
        Function for the User to provide functionality of Update, View and Delete Account.
    """
    global uid, pas, statusbtn_var, fname, lname, email, status, status_btn

    # Text-Widgets for Displaying the Info and Results.
    text_widget = tk.scrolledtext.ScrolledText(win, width=12, height=6)     # Text-Widget Variable
    
    lb1 = tk.Label(win, text="Database App")
    lb1.config(font=("Source Code Pro", 28))
    lb1.grid(row=0, columnspan=4, ipadx=60, ipady=20)

    lb2 = tk.Label(win, text="------------ Your Details -----------")
    lb2.grid(row=1, columnspan=4, sticky="news")

    extract_info(user)

    # ------------- Form Labels and Inputs --------------

    lb2 = tk.Label(win, text="FIRSTNAME : ")
    lb2.config(font=("Source Code Pro", 10))
    lb2.grid(row=2, column=0, sticky="e")

    fname = tk.Entry(win, textvariable=fname_var, state=DISABLED)
    fname.grid(row=2, column=1, pady=2, ipadx=70, sticky="nws")

    lb3 = tk.Label(win, text="LASTNAME : ")
    lb3.config(font=("Source Code Pro", 10))
    lb3.grid(row=3, column=0, sticky="e")

    lname = tk.Entry(win, textvariable=lname_var, state=DISABLED)
    lname.grid(row=3, column=1, pady=2, ipadx=70, sticky="nws")

    lb4 = tk.Label(win, text="USER-ID : ")
    lb4.config(font=("Source Code Pro", 10))
    lb4.grid(row=4, column=0, sticky="e")

    uid = tk.Entry(win, textvariable=uid_var, state=DISABLED)
    uid.grid(row=4, column=1, pady=2, ipadx=70, sticky="nws")

    lb5 = tk.Label(win, text="PASSWORD : ")
    lb5.config(font=("Source Code Pro", 10))
    lb5.grid(row=5, column=0, sticky="e")

    pas = tk.Entry(win, textvariable=pas_var, state=DISABLED)
    pas.config(show='*')
    pas.grid(row=5, column=1, pady=2, ipadx=70, sticky="nws")

    lb6 = tk.Label(win, text="EMAIL : ")
    lb6.config(font=("Source Code Pro", 10))
    lb6.grid(row=6, column=0, sticky="e")

    email = tk.Entry(win, textvariable=email_var, state=DISABLED)
    email.grid(row=6, column=1, pady=2, ipadx=70, sticky="nws")

    # --------------------------------------------------------

    # ----------------- Information Text Block ---------------
    text_widget.insert('insert', """To Make Changes to any of the Input Fields(Except USER-ID and PASSWORD) just Press the LOCKED button and then type in the new Entries and then Press UPDATE button!!""")
    text_widget.grid(row=7, columnspan=2, padx=10, pady=20, sticky="news")
    text_widget.config(state="disabled")

    # ----------------- Buttons --------------------

    frame_btns = tk.Frame(win)
    frame_btns.grid(row=8, columnspan=3)

    style.configure(SUNKABLE_BUTTON, foreground='green')

    statusbtn_var.set("LOCKED")

    status_btn = ttk.Button(frame_btns, textvariable=statusbtn_var, style=SUNKABLE_BUTTON, compound="left")
    status_btn.config(image=img)
    status_btn.bind("<Button-1>", lambda x: pass_verify(pas.get()))
    status_btn.grid(row=0, column=0)

    update_btn = ttk.Button(frame_btns, text="Update", style=SUNKABLE_BUTTON)
    update_btn.bind("<Button-1>", lambda x: update_user(fname.get(), lname.get(), uid.get(), pas.get(), email.get()))
    update_btn.grid(row=0, column=1)




create_login_screen()
win.mainloop()