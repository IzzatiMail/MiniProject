from tkinter import *
from  tkinter import ttk
import tkinter as tk

#################### FRAME ###########################################################################
window = Tk()
window.geometry("1200x1200")
window.title("TRY")
dobi_frame = Frame(window, width = 1200, height = 30, bg = 'green')
dobi_frame.pack(fill = tk.X, side = tk.TOP)
frm1 = Frame(window, width=600, height=203.333333, bg = 'green')
frm1.pack(fill=tk.Y, side= tk.LEFT)

################### LABEL ############################################################################

lbl = Label(dobi_frame, text='WELCOME TO LAUNDRY SERVICES UNIMAP ',font="Times 14 bold italic", bg = 'green')
lbl.pack()
lbl = Label(dobi_frame, text='FOR ANY INQUIRY, PLEASE CONTACT +60112954729',font="Times 8 bold italic", bg = 'green')
lbl.pack()
lbl2 = Label(frm1, text="\n\n\nPRICING:  \n\n\n\n\nWASH - RM 2.50 PER HOUR \n\nDRY - RM 2.50 PER HOUR",font='Helvetica 14 bold', bg = 'green')
lbl2.pack(anchor=CENTER,padx=20,pady=20)
label1 = Text(frm1)
#label1.insert("2.0","Wash - RM 2.50 PER HOUR  \n\nDRY - RM 2.50 PER HOUR")
#label1.pack()
window.mainloop()


