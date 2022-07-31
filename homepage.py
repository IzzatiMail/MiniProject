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

def clear_input():
    name.delete(0,END)
    matrix.delete(0,END)
    combo_type.set('')
    combo_blok.set('')
    combo_machine.set('')
    date.delete(0,END)
    combo_time1.set('')
    combo_time2.set('')

###################Frame###########################################################################
###################Dobi Frame###########################################################################
dobi_frame = Frame(window, width=1200, height=30, bg="#27408B")
dobi_frame.place(x=70,y=10,height=300)

lblTitle=Label(dobi_frame,width=47,height=2,relief=tk.RAISED,borderwidth=15,font=('Georgia',32,'bold'),text="Welcome to UNIMAP'S Laundromat",bg="#E3CF57",fg="#00008B")
lblTitle.grid(row=0,column=0,pady=10)
lbl = Label(dobi_frame, text='FOR ANY INQUIRY, PLEASE CONTACT +60112954729',font=('Georgia',12,'bold'),bg="black",fg="White")
lbl.grid(row=1,column=0,pady=0)

###################Price Frame###########################################################################
frm1 = Frame(window, width=250, height=500, bg="snow")
frm1.place(x=10,y=250,width=250, height=500)

lbl2 = Label(frm1, text="\nPRICING:",font='Helvetica 14 bold', bg="snow")
lbl2.grid(row=0,column=0,pady=20,padx=30)
lbl3 = Label(frm1, text="\n\nWASH - \n\n\nRM 2.50 PER HOUR",font='Helvetica 14 bold', bg="snow")
lbl3.grid(row=1,column=0,pady=20,padx=30)
lbl4 = Label(frm1, text="\n\nDRY - \n\n\nRM 2.50 PER HOUR",font='Helvetica 14 bold', bg="snow")
lbl4.grid(row=2,column=0,pady=20,padx=30)
###################Booking Frame###########################################################################
frm2 = Frame(window, width=600, height=500, bg="snow")
frm2.place(x=270,y=250,width=600,height=500)

book_t = Label(frm2, text="Booking's Details", font='Arial 18 bold', bg="snow")
book_t.grid(row=0,column=0,sticky=W,pady=20,padx=10)

lblname = Label(frm2, text='Name', font='Arial 12 bold', bg="snow")
lblname.grid(row=1,column=0,sticky=W,pady=5,padx=15)

name = Entry(frm2, textvariable=var_name,width=40, font='Arial 12', bg="#E0FFFF")
name.grid(row=1,column=1,sticky=W)

lblmatrix = Label(frm2, text='Matrix Number', font='Arial 12 bold', bg="snow")
lblmatrix.grid(row=2,column=0,sticky=W,pady=5,padx=15)

matrix = Entry(frm2, textvariable=var_id,width=30, font='Arial 12', bg="#E0FFFF")
matrix.grid(row=2,column=1,sticky=W)

type = Label(frm2, text='Type', font='Arial 12 bold', bg="snow")
type.grid(row=3,column=0,sticky=W,pady=5,padx=15)

combo_type=ttk.Combobox(frm2,textvariable=var_type,width=25,state="read", font='Arial 12 bold')
combo_type["value"]=("WASH", "DRY","BOTH")
combo_type.current()
combo_type.grid(row=3,column=1,sticky=W,pady=5)

blok = Label(frm2, text='Blok', font='Arial 12 bold', bg="snow")
blok.grid(row=4,column=0,sticky=W,pady=5,padx=15)

combo_blok=ttk.Combobox(frm2,textvariable=var_blok,width=25,state="read", font='Arial 12 bold')
combo_blok["value"]=("A1","A2","A3","A4")
combo_blok.current()
combo_blok.grid(row=4,column=1,sticky=W,pady=5)

machine = Label(frm2, text='Machine No', font='Arial 12 bold', bg="snow")
machine.grid(row=5,column=0,sticky=W,pady=5,padx=15)

combo_machine=ttk.Combobox(frm2,textvariable=var_machine,width=25,state="read", font='Arial 12 bold')
combo_machine["value"]=("1","2","3","4","5")
combo_machine.current()
combo_machine.grid(row=5,column=1,sticky=W,pady=5)

lbldate = Label(frm2, text='Date', font='Arial 12 bold', bg="snow")
lbldate.grid(row=6,column=0,sticky=W,pady=5,padx=15)

date = DateEntry(frm2, textvariable=var_date,date_pattern='yyyy-mm-dd',pady= 10, font='Arial 12 bold')
date.grid(row=6,column=1,sticky=W,pady=5)

time = Label(frm2, text='Time', font='Arial 12 bold', bg="snow")
time.grid(row=7,column=0,sticky=W,pady=5,padx=15)

combo_time1=ttk.Combobox(frm2,textvariable=var_timefrom,width=12,state="read", font='Arial 12 bold')
combo_time1["value"]=("06.00","07.00","08.00","09.00","10.00","11.00","12.00","13.00","14.00","15.00","16.00","17.00","18.00","19.00","20.00","21.00","22.00","23.00")
combo_time1.current()
combo_time1.grid(row=7,column=1,sticky=W)

time2 = Label(frm2, text='Until', font='Arial 12 bold', bg="snow")
time2.grid(row=7,column=1,sticky=W,pady=5,padx=150)

combo_time2=ttk.Combobox(frm2,textvariable=var_timeuntil,width=12,state="read", font='Arial 12 bold')
combo_time2["value"]=("06.00","07.00","08.00","09.00","10.00","11.00","12.00","13.00","14.00","15.00","16.00","17.00","18.00","19.00","20.00","21.00","22.00","23.00")
combo_time2.current()
combo_time2.grid(row=7,column=1,sticky=W,padx=200)

clear = Button(frm2, text="CLEAR", command=clear_input,fg="#00008B", bg="snow",font='Arial 12 bold',activebackground="grey")
clear.grid(row=8,column=0,sticky=W,pady=50,padx=15)

submit = Button(frm2, text="SUBMIT", command=cmd_submit,fg="#00008B", bg="#CAFF70",font='Arial 12 bold',activebackground="grey")
submit.grid(row=8,column=1,sticky=W,pady=50)

btn_exit=Button(frm2,text="EXIT",command=clicked,width=8, height = 1,bg="#FF4500",fg="white",font='Arial 12 bold',activebackground="grey")
btn_exit.grid(row=8,column=1,sticky=W,pady=50,padx=200)

###################Resit Frame###########################################################################
frm3 = Frame(window, width=650, height=500, bg="snow")
frm3.place(x=880,y=250,width=650,height=500)

book_t2 = Label(frm3, text="Booking's Details", font='Arial 18 bold', bg="snow")
book_t2.grid(row=0,column=0,sticky=W,pady=20,padx=10)

show=Button(frm3,text="REFRESH VIEW",command=view_data,width=15, height = 1,fg="#00008B", bg="snow",font='Arial 12 bold',activebackground="grey")
show.grid(row=0,column=0,sticky=W,pady=20,padx=480)

tbl = ttk.Treeview(frm3)
conn=sqlite3.connect('book.db')
with conn:
    cursor=conn.cursor()
cursor.execute("SELECT * FROM Booking")
rows = cursor.fetchall()
for row in rows:
    tbl.insert("", tk.END, values=row)
conn.commit()
conn.close()