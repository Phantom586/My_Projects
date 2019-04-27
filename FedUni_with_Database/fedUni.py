import tkinter as tk
from tkinter import *
from tkinter import messagebox, scrolledtext

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from moneymanager import MoneyManager

import sqlite3


# Creating the conection Object
conn = sqlite3.connect('records_bank.db')

# acquiring the cursor
c = conn.cursor()



win = tk.Tk()

#Set window size here to '540 x 640'
win.geometry('540x640')
win.minsize(540, 640)
win.maxsize(540, 640)

#Set the window title to 'FedUni Money Manager'
win.title("FedUni Money Manager")