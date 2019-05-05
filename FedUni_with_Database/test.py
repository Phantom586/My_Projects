import tkinter as tk
from tkinter import *

import tkinter.ttk as ttk

from tkinter import messagebox, scrolledtext

from MyDatabase import Database

my_db = Database('records_bank')



win = tk.Tk()

win.geometry('390x550')
win.minsize(390, 550)
win.maxsize(390, 550)

style = ttk.Style()

win.title("My Database App")

# ---------------------- Entry Widgets Variables -----------

fname_var = tk.StringVar()
lname_var = tk.StringVar()
uid_var = tk.StringVar()
pas_var = tk.StringVar()
email_var = tk.StringVar()
text_widget = tk.scrolledtext.ScrolledText(win, width=12, height=4)
text_widget_1 = tk.scrolledtext.ScrolledText(win, width=12, height=6)


# ---------------------- Buttons ---------------------------

preview_btn = ''
register_btn = ''
signin_btn = ''
search_btn = ''

SUNKABLE_BUTTON = 'SunkableButton.TButton'


# ----------------------- Functions -------------------------

def remove_all_widgets():
    '''Function to remove all the widgets from the window.'''
    global win
    for widget in win.winfo_children():
        widget.grid_remove()


def clear_pin_entries(des):

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
    my_db.create_table('account_details',
                        'user_fname text',
                        'user_lname text',
                        'user_id text',
                        'user_pass text',
                        'user_email text')


def add_user(fname, lname, u_id, u_pass, email):

    global register_btn

    flag = True

    if fname == '' and lname == '' and u_id == '' and u_pass == '' and email == '':
        messagebox.showerror('Error!!', 'Blank Fields are not Allowed!!')
    else:
        check = my_db.select_from_db('account_details', ['user_id', 'user_pass'])
        print(check)
        for entries in check:
            if u_id and u_pass in entries:
                flag = False
                messagebox.showwarning('Field Error!!', "Please! Use Another Username and Password!!")
                clear_pin_entries('userpass')
                break

        if flag:
            my_db.insert_into_db('account_details',fname, lname, u_id, u_pass, email)
            clear_pin_entries('cred')
            messagebox.showinfo('User Accounts', 'User has been Added Successfully!')



def validate_user(u_id, u_pass):

    global search_btn

    if u_id != '' and u_pass != '':
        d = my_db.select_from_db('account_details', user_id=u_id, user_pass=u_pass)
        if d:
            print("User Exists!!!")
                
        else:
            print("User Doesn't Exists!!!")
            clear_pin_entries('')
            messagebox.showerror('Login Error!!', 'Sorry! The User doesn\'t Exists!')
    else:
        messagebox.showerror('Error!!', 'Blank Fields are not Allowed!!')

        

def query_db():
    # c = my_db.select_from_db('account_details')
    c = my_db.select_from_db('account_details', user_id='1716410101')
    # c = my_db.select_from_db('account_details', ['user_id', 'user_pass'])
    # for values in c:
    #     print(values)
    print(c)


def preview(u_id, u_pass):

    if u_id != '' and u_pass != '':
        result = my_db.select_from_db('account_details', user_id=u_id, user_pass=u_pass)
        # print(result)
        output_win(result, "Preview Results : ")
    else:
        messagebox.showerror('Error!!', 'Blank Fields are not Allowed!!')


def search(u_fname, u_id):

    lst = [['u_fname', u_fname], ['u_id', u_id]]

    # Checking which of the inputs are to be inserted in the Query
    lst = [i for i in lst if i[1] != '']

    if lst != []:
        if len(lst) == 1:
            if lst[0][1] == 'u_fname':
                result = my_db.select_from_db('account_details', user_fname=u_fname)
            else:
                result = my_db.select_from_db('account_details', user_id=u_id)
        else:
            result = my_db.select_from_db('account_details', user_id=u_id, user_fname=u_fname)

    output_win(result, "Search Results :")

    


def output_win(str, msg):

    text_widget_2 = tk.scrolledtext.ScrolledText(win, width=12, height=6)
    
    text_widget_2.insert('insert', f'-------- {msg} --------' + '\n')
    for text in str:
        for txt in text:
            text_widget_2.insert('insert', txt + '\n')
            text_widget_2.insert('insert', '-----------------------' + '\n')
    text_widget_2.grid(row=9, columnspan=2, padx=10, sticky="news")
    text_widget_2.config(state="disabled")


def shortcuts(param):
    if param == "quit":
        win.destroy()


# ---------------------- Key Shortcuts ------------------
win.bind("<Control-q>", lambda e:shortcuts("quit"))

my_db.create_db()
# create_table()
# my_db.remove_from_db('account_details', False, user_id=1716410101, user_pass=1234)
# my_db.drop_table('account_details')
# query_db()



# --------------- User Interface Functions ----------------

def create_login_screen():

    global fname_var, lname_var, uid_var, pas_var, email_var, search_btn, preview_btn, register_btn, signin_btn, SUNKABLE_BUTTON
    global text_widget_1

    lb1 = tk.Label(win, text="Database App")
    lb1.config(font=("Source Code Pro", 28))
    lb1.grid(row=0, columnspan=2, ipadx=60, ipady=20)

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

    text_widget.insert('insert', """USER-ID and PASSWORD are unique for everyone!!\nFor SignIn Only USER-ID and PASSWORD Fields are required!!""")
    text_widget.grid(row=6, columnspan=2, padx=10, pady=20, sticky="news")
    text_widget.config(state="disabled")

    frame_btns = tk.Frame(win)
    frame_btns.grid(row=7, columnspan=3)

    style.configure(SUNKABLE_BUTTON, foreground='green')

    preview_btn = ttk.Button(frame_btns, text="Preview", style=SUNKABLE_BUTTON)
    preview_btn.bind("<Button-1>", lambda x: preview(uid.get(), pas.get()))
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

    lb7 = Label(win, text="OUTPUT : ")
    lb7.grid(row=8, columnspan=2, pady=20)

    text_widget_1.insert('insert', """This is Output Window""")
    text_widget_1.grid(row=9, columnspan=2, padx=10, sticky="news")
    text_widget_1.config(state="disabled")

    lb8 = Label(win, text="Press 'Ctrl+q' to Quit the App.")
    lb8.grid(row=10, columnspan=2, pady=20)


def create_user_screen():

    lb1 = tk.Label(win, text="Database App")
    lb1.config(font=("Source Code Pro", 28))
    lb1.grid(row=0, columnspan=4, ipadx=160, ipady=20)




create_login_screen()
win.mainloop()