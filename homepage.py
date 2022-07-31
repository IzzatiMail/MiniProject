############          mini project              ############################################
############          import library            ############################################
from ast import pattern
import sqlite3
from tkinter import *
from  tkinter import ttk
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox

#exit button
def clicked ():
    iQuit=messagebox.askyesno("Bye Bye",  "Are you sure you want to quit?")
    if iQuit > 0:
        window.destroy()
    return

#submit button
def cmd_submit():
    if var_name.get()==""or var_id.get()==""or var_type.get()=="" or var_blok.get()=="" or var_machine.get()=="" or var_timefrom.get()=="" or var_timeuntil.get()=="":
        messagebox.showerror("Error","Please Fill All the Details")
    else:
        #get var
        dbname=var_name.get()
        dbmatrix=var_id.get()
        dbtype=var_type.get()
        dbblok=var_blok.get()
        dbmachine=var_machine.get()
        dbdate=var_date.get()
        dbfrom=var_timefrom.get()
        dbuntil=var_timeuntil.get()

        conn=sqlite3.connect('book.db')
        with conn:
            cursor=conn.cursor()
        #insert records    
        cursor.execute('INSERT INTO Booking (NAME,MATRIX,TYPE,BLOK,MACHINE,DATE,T_FROM,T_UNTIL) VALUES(?,?,?,?,?,?,?,?)',(dbname,dbmatrix,dbtype,dbblok,dbmachine,dbdate,dbfrom,dbuntil))
        print("Records insert successfully")
        
        #view records
        for record in tbl.get_children():
            tbl.delete(record)
        cursor.execute("SELECT * FROM Booking")
        rows = cursor.fetchall()
        for row in rows:
            tbl.insert("", tk.END, values=row)
        if var_type.get()=="WASH":
            messagebox.showinfo("Payment","We have received your booking.\n Please pay RM2.50 at the nearest machine")
        elif var_type.get()=="DRY":
            messagebox.showinfo("Payment","We have received your booking.\n Please pay RM2.50 at the nearest machine")
        else:
            messagebox.showinfo("Payment","We have received your booking.\n Please pay RM5.00 at the nearest machine")
        print("Records shown successfully")
        name.delete(0,END)
        matrix.delete(0,END)
        combo_type.set('')
        combo_blok.set('')
        combo_machine.set('')
        date.delete(0,END)
        combo_time1.set('')
        combo_time2.set('')
        conn.commit()
        conn.close()

#view data in database
def view_data():
    #clear duplicate data in table
    for record in tbl.get_children():
        tbl.delete(record)
    conn=sqlite3.connect('book.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute("SELECT * FROM Booking")
    rows = cursor.fetchall()
    for row in rows:
        tbl.insert("", tk.END, values=row)
    conn.close()

#find selected data from matrix in database
def find_data():
    #clear duplicate data in table
    tbl.selection()
    fetchdata=tbl.get_children()
    for f in fetchdata:
        tbl.delete(f)
    conn=None
    try:
        conn=sqlite3.connect('book.db')
        cursor=conn.cursor()
        db="SELECT * FROM Booking WHERE MATRIX='%s'"
        var_mat=findmatrix.get()
        if(not var_mat.isnumeric()):
            messagebox.showerror("FAIL","Invalid Matrix or Wrong Matrix No")
        else:
            cursor.execute(db %(var_mat))
            data=cursor.fetchall()
            for d in data:
                tbl.insert("",END,values=d) 
    except EXCEPTION as e:
        messagebox.showerror("ISSUE",e)
    finally:
        if conn is not None:
            conn.close()
    findmatrix.delete(0,END)
    ###################Configure Window###########################################################################
window = Tk()
window.title('Welcome')
window.configure(bg="#27408B")
window.attributes('-fullscreen', True)
window.minsize(width = 1370, height = 700)
window.maxsize(width = 1370, height = 700)

####Var####
var_name=StringVar()
var_id=StringVar()
var_type=StringVar()
var_blok=StringVar()
var_machine=StringVar()
var_date=StringVar()
var_timefrom=StringVar()
var_timeuntil=StringVar()
var_mat=StringVar()
var_delid=StringVar()