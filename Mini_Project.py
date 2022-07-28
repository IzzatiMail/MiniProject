from cgitb import text
from datetime import timezone
from re import T
from tkinter import *
from  tkinter import ttk
from turtle import left, right, width
import tkinter as tk
from tkcalendar import DateEntry

def clicked ():
    window.destroy()
################### FRAME ###########################################################################
window = Tk()
window.title('Welcome - Price')
window.geometry("1285x1200")
#window.resizable(0,0)
#dobi_frame = Frame(window, width=1200, height=30, bg="snow")
#dobi_frame.pack(fill=tk.X, side=tk.TOP)
#frm1 = Frame(window, width=600, height=203.333333, bg="snow")
#frm1.pack(fill=tk.Y, side= tk.LEFT)
frm2 = Frame(width=900, height=203.333333, bg="snow")
frm2.pack(fill=tk.Y, side=tk.LEFT)
frm3 = Frame(width=900, height=203.333333, bg="snow")
frm3.pack(fill=tk.Y, side=tk.LEFT)
tbl = ttk.Treeview(frm3)


################### LABEL ############################################################################

#lbl = Label(dobi_frame, text='WELCOME TO LAUNDRY SERVICES UNIMAP ',font="Times 14 bold italic", bg="snow")
#lbl.pack()
#lbl = Label(dobi_frame, text='FOR ANY INQUIRY, PLEASE CONTACT +60112954729',font="Times 8 bold italic", bg="snow")
#lbl.pack()
#lbl2 = Label(frm1, text="\n\n\nPRICING:  \n\n\n\n\nWASH - RM 2.50 PER HOUR \n\nDRY - RM 2.50 PER HOUR",font='Helvetica 14 bold', bg="snow")
#lbl2.pack(anchor=CENTER,padx=20,pady=20)
#label1 = Text(frm1)
#label1.insert("2.0","Wash - RM 2.50 PER HOUR  \n\nDRY - RM 2.50 PER HOUR")
#label1.pack()
lbl3 = Label(frm3, text='BOOK LIST :', font="Courier 14 italic", bg="snow")
lbl3.pack(side='top')
name = Label(frm2, text='Name', font='Arial 10 bold', bg="snow")
name.pack()
name = Entry(frm2,width=50)
name.pack(padx=10,pady=10)
matrix = Label(frm2, text='Id', font='Arial 10 bold', bg="snow")
matrix.pack()
matrix = Entry(frm2,width=50)
matrix.pack()

#################### BUTTON ##########################################################################

drop= StringVar()
drop.set("Type")
drop= OptionMenu(frm2, drop,"Wash", "Dry","Both")
drop.pack(fill='y',pady=10)
drop2 = StringVar()
drop2.set("Block")
drop2= OptionMenu(frm2, drop2,"A1","A2","A3","A4")
drop2.pack(fill='y', pady=10)
drop3 = StringVar()
drop3.set("Machine No.")
drop3 = OptionMenu(frm2, drop3,"1","2","3","4","5")
drop3.pack(fill='y', pady=10)
drop4 = Label(frm2,text='Date',font='Arial 10 bold',bg='snow')
drop4.pack()
drop4 = DateEntry(frm2, pady= 10)
drop4.pack()
drop5 = StringVar()
drop5.set("Time")
drop5 = OptionMenu(frm2, drop5,"12.00-01.00","01.00-02.00","02.00-03.00","03.00-04.00","05.00-06.00","06.00-07.00","07.00-08.00","08.00-09.00","09.00-10.00","10.00-11.00","11.00-12.00")
drop5.pack()
drop6 = StringVar()
drop6.set("AM")
drop6 = OptionMenu(frm2,drop6,"AM","PM")
drop6.pack()
submit = Button(frm2, text="Submit", command=clicked, bg="light green",)
submit.pack(padx=15,pady=10)
################### LABEL ############################################################################

#lbl4 = Label(frm2, text="Time")
#lbl4.pack()
#lbl4 = Entry(frm2)
#lbl4.pack(side='left')
#lbl5 = Entry(frm2)
#lbl5.pack(side='right')

#drop4 = IntVar()
#drop4.set("Time")
#drop4 = OptionMenu(frm4, drop4,"12.00-1.00","1.00-2.00","2.00-3.00","3.00-4.00","4.00-5.00","5.00-6.00","6.00-7.00","7.00-8.00","8.00-9.00","9.00-10.00","10.00-11.00","11.00-12.00")
#drop4.pack(side='left',fill='x', expand=False, padx=10)
#drop5 = StringVar()
#drop5.set("")
#drop5 = OptionMenu(frm4, drop5, "AM","PM")
#drop5.pack(side='right', pady=0,)


################### TABLE ############################################################################

tbl['columns'] = ('JS', 'p', 'matrix', 'blok', 'time', 'tarikh', 'machine')

tbl.column("#0", width=0,  stretch=NO)
tbl.column("JS",anchor=CENTER, width=60)
tbl.column("p",anchor=CENTER,width=100)
tbl.column("matrix",anchor=CENTER,width=100)
tbl.column("blok",anchor=CENTER, width=80)
tbl.column("time",anchor=CENTER,width=100)
tbl.column("tarikh",anchor=CENTER,width=100)
tbl.column("machine",anchor=CENTER,width=100)
tbl.heading("JS",text="No",anchor=CENTER)
tbl.heading("p",text="Name",anchor=CENTER)
tbl.heading("matrix",text="Id",anchor=CENTER)
tbl.heading("blok",text="Block",anchor=CENTER)
tbl.heading("time",text="Time",anchor=CENTER)
tbl.heading("tarikh",text="Date",anchor=CENTER)
tbl.heading("machine",text="Machine No.",anchor=CENTER)
tbl.pack(fill='both', padx=10,pady=10)
window.mainloop()