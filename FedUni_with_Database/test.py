import tkinter as tk
from tkinter import *

from tkinter import messagebox, scrolledtext

from MyDatabase import Database

my_db = Database('records_bank')



win = tk.Tk()

win.geometry('400x350')
win.minsize(400, 350)
win.maxsize(400, 350)

win.title("My Database App")

# ---------------------- Entry Widgets Variables -----------

fname_var = tk.StringVar()
lname_var = tk.StringVar()
uid_var = tk.StringVar()
pas_var = tk.StringVar()
email_var = tk.StringVar()
text_widget = tk.scrolledtext.ScrolledText(win, width=12, height=2)


# ----------------------- Functions -------------------------

def remove_all_widgets():
    '''Function to remove all the widgets from the window.'''
    global win
    for widget in win.winfo_children():
        widget.grid_remove()


def clear_pin_entries(des):

    global fname_var, lname_var, uid_var, pas_var, email_var

    fname_var.set('')
    lname_var.set('')
    email_var.set('')

    if des == 'all':
        uid_var.set('')
        pas_var.set('')


def create_table():
    my_db.create_table('account_details', 'user_fname text', 'user_lname text', 'user_id integer', 'user_pass integer', 'user_email text')


def add_user(fname, lname, u_id, u_pass, email):

    flag = True

    if fname == '' and lname == '' and u_id == '' and u_pass == '' and email == '':
        messagebox.showerror('Error!!', 'Blank Fields are not Allowed!!')
    else:
        check = my_db.select_from_db('account_details', ['user_id', 'user_pass'])
        print(check)
        for entries in check:
            if u_id in entries and u_pass in entries:
                flag = False
                messagebox.showwarning('Field Error!!', "Please! Use Another Username and Password!!")

        if flag:
            my_db.insert_into_db('account_details',fname, lname, u_id, u_pass, email)
            clear_pin_entries('')
            messagebox.showinfo('User Accounts', 'User has been Added Successfully!')


def validate_user(u_id, u_pass):
    d = my_db.select_from_db('account_details', user_id=u_id, user_pass=u_pass)
    if d:
        print("User Exists!!!")
        
    else:
        print("User Doesn't Exists!!!")
        clear_pin_entries('all')
        messagebox.showerror('Login Error!!', 'Sorry! The User doesn\'t Exists!')


def query_db():
    c = my_db.select_from_db('account_details')
    # c = my_db.select_from_db('account_details', ['user_id', 'user_pass'])
    # for values in c:
    #     print(values)
    print(c)



my_db.create_db()
# create_table()
# my_db.remove_from_db('account_details', False, user_id=1716410101, user_pass=1234)
# my_db.drop_table('account_etails')
query_db()



# --------------- User Interface Functions ----------------

def create_login_screen():

    global fname_var, lname_var, uid_var, pas_var, email_var

    lb1 = tk.Label(win, text="Database App")
    lb1.config(font=("Source Code Pro", 28))
    lb1.grid(row=0, columnspan=2, ipadx=60, ipady=20)

    lb2 = tk.Label(win, text="FIRSTNAME : ")
    lb2.config(font=("Source Code Pro", 10))
    lb2.grid(row=1, column=0,ipadx=10, sticky="e")

    fname = tk.Entry(win, textvariable=fname_var)
    fname.grid(row=1, column=1, sticky="news")

    lb3 = tk.Label(win, text="LASTNAME : ")
    lb3.config(font=("Source Code Pro", 10))
    lb3.grid(row=2, column=0,ipadx=10, sticky="e")

    lname = tk.Entry(win, textvariable=lname_var)
    lname.grid(row=2, column=1, sticky="news")

    lb4 = tk.Label(win, text="USER-ID : ")
    lb4.config(font=("Source Code Pro", 10))
    lb4.grid(row=3, column=0,ipadx=10, sticky="e")

    uid = tk.Entry(win, textvariable=uid_var)
    uid.grid(row=3, column=1, sticky="news")

    lb5 = tk.Label(win, text="PASSWORD : ")
    lb5.config(font=("Source Code Pro", 10))
    lb5.grid(row=4, column=0,ipadx=10, sticky="e")

    pas = tk.Entry(win, textvariable=pas_var)
    pas.config(show="*")
    pas.grid(row=4, column=1, sticky="news")

    lb6 = tk.Label(win, text="EMAIL : ")
    lb6.config(font=("Source Code Pro", 10))
    lb6.grid(row=5, column=0,ipadx=10, sticky="e")

    email = tk.Entry(win, textvariable=email_var)
    email.grid(row=5, column=1, sticky="news")

    text_widget.insert('insert', 'For SignIn Only USER-ID and PASSWORD Fields are required!!')
    text_widget.grid(row=6, columnspan=2, padx=10, pady=20, sticky="news")
    text_widget.config(state="disabled")

    bt1 = tk.Button(win, text="Register", bg="green", activebackground="green")
    bt1.bind("<Button-1>", lambda x: add_user(fname.get(), lname.get(), uid.get(), pas.get(), email.get()))
    bt1.grid(row=7, column=0, padx=10, pady=15, sticky="news")

    bt1 = tk.Button(win, text="SignIn", bg="green", activebackground="green")
    bt1.bind("<Button-1>", lambda x: validate_user(uid.get(), pas.get()))
    bt1.grid(row=7, column=1, padx=10, pady=15, sticky="news")


def create_user_screen():

    lb1 = tk.Label(win, text="Database App")
    lb1.config(font=("Source Code Pro", 28))
    lb1.grid(row=0, columnspan=4, ipadx=160, ipady=20)




# create_login_screen()
win.mainloop()