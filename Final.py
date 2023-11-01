import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql

#Functuons 

def check():
    global password
    password = input("Enter database password: \n")
    con = mysql.connect(host='localhost', user='root', passwd=password)
    cur = con.cursor()
    cur.execute("create database if not exists mysch")
    cur.execute("use mysch")
    cur.execute('''CREATE TABLE IF NOT EXISTS students (
    rollno VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    grade VARCHAR(255),
    sec VARCHAR(255),
    phone VARCHAR(255),
    guardian VARCHAR(255),
    gender VARCHAR(255),
    dob VARCHAR(255),
    area VARCHAR(255)
);''')
    con.commit()
    con.close()

def fetch_data():
    con = mysql.connect(host='localhost', user='root', passwd=password, database = "mysch")
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    if len(data) != 0:
        table.delete(*table.get_children())
        for i in data:
            table.insert('', tk.END, values = i)
        con.commit()
    con.close()

def add_data():
    con = mysql.connect(host='localhost', user='root', passwd=password, database = "mysch")
    cur = con.cursor()
    cur.execute("SELECT rollno FROM students")
    data = cur.fetchall()
    data = [i[0] for i in data]
    if rollno.get() == "" or name.get()== "" or grade.get()== "" or sec.get()== "" or phone.get()== "" or guardian.get()== "" or gender.get()== "" or dob.get()== "" or area.get()== "":
        messagebox.showerror("Error!", "Please fill out all given fields!")
    elif rollno.get() in data:
        messagebox.showerror("Error!", "That Roll Number is already in use. Please enter a correct roll number!")
        
    else:     
        cur.execute("INSERT INTO students VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (rollno.get(), name.get(), grade.get(), sec.get(), phone.get(), guardian.get(), gender.get(), dob.get(), area.get()))
        con.commit()
        fetch_data()
    con.close()

def update_current_data(event):
    row = table.focus()
    items = table.item(row)
    data = items['values']
    rollno.set(data[0])
    name.set(data[1])
    grade.set(data[2])
    sec.set(data[3])
    phone.set(data[4])
    guardian.set(data[5])
    gender.set(data[6])
    dob.set(data[7])
    area.set(data[8])

def clear_data():
    rollno.set("")
    name.set("")
    grade.set("")
    sec.set("")
    phone.set("")
    guardian.set("")
    gender.set("")
    dob.set("")
    area.set("")

def update_data():
    con = mysql.connect(host='localhost', user='root', passwd=password, database = "mysch")
    cur = con.cursor()
    cur.execute("UPDATE students SET name = %s, grade = %s, sec = %s, phone = %s, guardian = %s, gender = %s, dob = %s, area = %s WHERE rollno = %s", (name.get(), grade.get(), sec.get(), phone.get(), guardian.get(), gender.get(), dob.get(), area.get(), rollno.get()))
    con.commit()
    con.close()
    fetch_data()

def delete_data():
    con = mysql.connect(host='localhost', user='root', passwd=password, database = "mysch")
    cur = con.cursor()
    cur.execute("DELETE from students WHERE rollno = %s", (rollno.get(),))
    con.commit()
    con.close()
    selected_item = table.selection()[0] ## get selected item
    table.delete(selected_item)
    clear_data()

def treeview_sort_column(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)

    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    tv.heading(col, command=lambda: \
               treeview_sort_column(tv, col, not reverse))


# Main Body
check()
root = tk.Tk()
root.geometry("1350x700+0+0")
root.title("CPS Management System")

title = tk.Label(root, text = "Chavara Public School", font = ("Arial", 25, "bold"), border = 12, relief=tk.GROOVE, background= "#add8e6")
title.pack(side = tk.TOP, fill = tk.X)

details = tk.LabelFrame(root, text = "Enter Details", font = ("Arial", 25), background= "#add8e6", border = 12, relief = tk.GROOVE)
details.place(x = 20, y = 90, width=480, height=600)

display = tk.Frame(root, border = 12, background="#add8e6", relief = tk.GROOVE)
display.place(x = 520, y = 90, width = 810, height = 600)

# Variables
rollno = tk.StringVar()
name = tk.StringVar()
grade = tk.StringVar()
sec = tk.StringVar()
phone = tk.StringVar()
guardian = tk.StringVar()
area = tk.StringVar()
gender = tk.StringVar()
dob = tk.StringVar()

search_with = tk.StringVar()


# Entry area
rollno_box = tk.Label(details, text = "Roll No:", font = ("Arial", 17), background= "#add8e6")
rollno_box.grid(row=0, column = 0, padx = 2, pady=2)

rollno_ent = tk.Entry(details, border = 7, font = ("Arial, 17"), textvariable=rollno)
rollno_ent.grid(row=0, column = 1, padx = 2, pady=2)

name_box = tk.Label(details, text = "Name:", font = ("Arial", 17), background= "#add8e6")
name_box.grid(row=1, column = 0, padx = 2, pady=2)

name_ent = tk.Entry(details, border = 7, font = ("Arial, 17"), textvariable= name)
name_ent.grid(row=1, column = 1, padx = 2, pady=2)

grade_box = tk.Label(details, text = "Grade:", font = ("Arial", 17), background= "#add8e6")
grade_box.grid(row=2, column = 0, padx = 2, pady=2)

grade_ent = tk.Entry(details, border = 7, font = ("Arial, 17"), textvariable= grade)
grade_ent.grid(row=2, column = 1, padx = 2, pady=2)

div_box = tk.Label(details, text = "Division:", font = ("Arial", 17), background= "#add8e6")
div_box.grid(row=3, column = 0, padx = 2, pady=2)

div_ent = tk.Entry(details, border = 7, font = ("Arial, 17"), textvariable= sec)
div_ent.grid(row=3, column = 1, padx = 2, pady=2)

phone_box = tk.Label(details, text = "Phone Number:", font = ("Arial", 17), background= "#add8e6")
phone_box.grid(row=4, column = 0, padx = 2, pady=2)

phone_ent = tk.Entry(details, border = 7, font = ("Arial, 17"), textvariable=phone)
phone_ent.grid(row=4, column = 1, padx = 2, pady=2)

guard_box = tk.Label(details, text = "Guardian:", font = ("Arial", 17), background= "#add8e6")
guard_box.grid(row=5, column = 0, padx = 2, pady=2)

guard_ent = tk.Entry(details, border = 7, font = ("Arial, 17"), textvariable=guardian)
guard_ent.grid(row=5, column = 1, padx = 2, pady=2)

area_box = tk.Label(details, text = "Address:", font = ("Arial", 17), background= "#add8e6")
area_box.grid(row=6, column = 0, padx = 2, pady=2)

area_ent = tk.Entry(details, border = 7, font = ("Arial, 17"), textvariable=area)
area_ent.grid(row=6, column = 1, padx = 2, pady=2)

gender_box = tk.Label(details, text = "Gender:", font = ("Arial", 17), background= "#add8e6")
gender_box.grid(row=7, column = 0, padx = 2, pady=2)

gender_ent = ttk.Combobox(details, font = ("Arial", 17), state = "readonly", textvariable=gender)
gender_ent['values'] = "Male", "Female", "Other"
gender_ent.grid(row=7, column = 1, padx = 2, pady=2)

dob_box = tk.Label(details, text = "Date of Birth:", font = ("Arial", 17), background= "#add8e6")
dob_box.grid(row=8, column = 0, padx = 2, pady=2)

dob_ent = tk.Entry(details, border = 7, font = ("Arial, 17"), textvariable=dob)
dob_ent.grid(row=8, column = 1, padx = 2, pady=2)

btn_frame = tk.Frame(details, border = 10, relief=tk.GROOVE)
btn_frame.place(x = 20, y = 410, width = 400, height = 130)

add_btn = tk.Button(btn_frame, text = "Add", border = 7, font = ("Arial", 15), width = 15, background= "#add8e6", command=add_data)
add_btn.grid(row = 0, column = 0, padx = 2, pady=2)

update_btn = tk.Button(btn_frame, text = "Update", border = 7, font = ("Arial", 15), width = 15, background= "#add8e6", command = update_data)
update_btn.grid(row = 0, column = 1, padx = 2, pady=2)

delete_btn = tk.Button(btn_frame, text = "Delete", border = 7, font = ("Arial", 15), width = 15, background= "#add8e6", command = delete_data)
delete_btn.grid(row = 1, column = 1, padx = 2, pady=2)

clear_btn = tk.Button(btn_frame, text = "Clear", border = 7, font = ("Arial", 15), width = 15, background= "#add8e6", command = clear_data)
clear_btn.grid(row = 1, column = 0, padx = 2, pady=2)

#Search

search_frame = tk.Frame(display, border = 10, relief=tk.GROOVE, background= "#add8e6")
search_frame.pack(side = tk.TOP, fill = tk.X)

search_label = tk.Label(search_frame, text = "Search:", font = ("Arial", 17), background= "#add8e6")
search_label.grid(row = 0, column = 0, padx = 12, pady = 2)

search_in = ttk.Combobox(search_frame, font = ("Arial", 17), state = "readonly", textvariable=search_with)
search_in['values'] = ("Name", "Roll No.", "Phone No.", "Guardian's Name", "Grade", "Division", "Date of Birth")
search_in.grid(row= 0, column = 1, padx = 12, pady = 2)

search_btn = tk.Button(search_frame, text = "Search!", font = ("Arial", 15), border = 9, width = 12, background= "#add8e6")
search_btn.grid(row = 0, column = 2, padx=12, pady = 2)

showall_btn = tk.Button(search_frame, text = "Show All", font = ("Arial", 15), border = 9, width = 12, background= "#add8e6")
showall_btn.grid(row = 0, column = 3, padx=12, pady = 2)


#Database Table
main = tk.Frame(display, background= "#add8e6", border = 12, relief=tk.GROOVE)
main.pack(fill = tk.BOTH, expand = True)

yscroll = tk.Scrollbar(main, orient = tk.VERTICAL)
xscroll = tk.Scrollbar(main, orient = tk.HORIZONTAL)

table = ttk.Treeview(main, columns = ("Roll No.", "Name", "Grade", "Division", "Phone No.", "Guardian's Name","Gender", "Date of Birth", "Address"), yscrollcommand = yscroll.set, xscrollcommand = xscroll.set)

yscroll.config(command = table.yview)
xscroll.config(command = table.xview)

yscroll.pack(side = tk.RIGHT, fill = tk.Y)
xscroll.pack(side = tk.BOTTOM, fill = tk.X)

table.heading("Roll No.", text = "Roll No.", command=lambda: \
                     treeview_sort_column(table, "Roll No.", False))
table.heading("Name", text = "Name", command=lambda: \
                     treeview_sort_column(table, "Name", False))
table.heading("Grade", text = "Grade", command=lambda: \
                     treeview_sort_column(table, "Grade", False))
table.heading("Division", text = "Division", command=lambda: \
                     treeview_sort_column(table, "Division", False))
table.heading("Phone No.", text = "Phone No.", command=lambda: \
                     treeview_sort_column(table, "Phone No.", False))
table.heading("Guardian's Name", text = "Guardian's Name", command=lambda: \
                     treeview_sort_column(table, "Guardian's Name", False))
table.heading("Gender", text = "Gender", command=lambda: \
                     treeview_sort_column(table, "Gender", False))
table.heading("Date of Birth", text = "Date of Birth", command=lambda: \
                     treeview_sort_column(table, "Date of Birth", False))
table.heading("Address", text = "Address", command=lambda: \
                     treeview_sort_column(table, "Address", False))
table['show'] = 'headings'

table.column("Roll No.", width=100)
table.column("Name", width=100)
table.column("Grade", width=100)
table.column("Division", width=100)
table.column("Phone No.", width=100)
table.column("Guardian's Name", width=100)
table.column("Gender", width=100)
table.column("Date of Birth", width=100)
table.column("Address", width=150)

table.pack(fill=tk.BOTH, expand = True)

fetch_data()
table.bind("<ButtonRelease-1>", update_current_data)
root.mainloop()