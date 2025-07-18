import tkinter as tk
from tkinter import ttk
import  openpyxl


root = tk.Tk()

style = ttk.Style(root)
root.tk.call("source", "forest-light.tcl")
root.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")

def toggle_mode():
    if mode_switch.instate(['selected']):
        style.theme_use('forest-light')
    else:
        style.theme_use('forest-dark')

def load_data():
    path = "D:\\MiniExcel-Python_GUI\people.xlsx"
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active

    list_values = list(sheet.values)
    print(list_values)

    for col_name in list_values[0]:
        treeView.heading(col_name, text=col_name)

    for value_tuple in list_values[1:]:
        treeView.insert('', tk.END, values=value_tuple)

def insert_row():
    name = name_entry.get()
    age = int(age_spinbox.get())
    subscription_status = status_combobox.get()
    employment_status ="Employed" if a.get() else "Unemployed"


#Insert row into excel sheet
    path = "D:\\MiniExcel-Python_GUI\people.xlsx"
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active 
    row_values = [name, age, subscription_status, employment_status]
    sheet.append(row_values)
# Insert row into treeView
    treeView.insert('', tk.END, values=row_values)  

    #Clear all values on entry
    name_entry.delete(0, tk.END)
    name_entry.insert(0, 'Name')
    age_spinbox.delete(0, tk.END)
    age_spinbox.insert(0, 'Age')
    status_combobox.set(combo_list[0])
    check_btn.state(['!selected'])
    

combo_list = ['Subscribed', 'Not Subscribed', 'Others']


frame = ttk.Frame(root)
frame.pack()

widgets_frame = ttk.LabelFrame(frame, text='Insert Row')
widgets_frame.grid(row=0, column=0, padx=20, pady=10)

name_entry = ttk.Entry(widgets_frame)
name_entry.insert(0, 'Name')
name_entry.bind("<FocusIn>", lambda e: name_entry.delete(0, tk.END))
name_entry.grid(row=0, column=0, padx=5, pady=(0,5),sticky="ew")

age_spinbox = ttk.Spinbox(widgets_frame, from_=18, to=100)
age_spinbox.insert(0, "Age")
age_spinbox.grid(row=1, column=0, padx=5, pady=(0,5), sticky="ew") 

status_combobox = ttk.Combobox(widgets_frame, values=combo_list)
status_combobox.current(0)
status_combobox.grid(row=2, column=0, padx=5, pady=(0,5), sticky="ew")

a = tk.BooleanVar()
check_btn = ttk.Checkbutton(widgets_frame, text='Employed', variable=a)
check_btn.grid(row=3, column=0, padx=5, pady=(0,5),sticky='nsew')

insert_btn = ttk.Button(widgets_frame, text='Insert', command=insert_row)
insert_btn.grid(row=4, column=0, padx=5, pady=(0,5), sticky='nsew') 

separator = ttk.Separator(widgets_frame)
separator.grid(row=5, column=0, padx=(20,10), pady=10,sticky='ew')



mode_switch = ttk.Checkbutton(widgets_frame, text='Mode', style='Switch', command=toggle_mode)
mode_switch.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")

treeFrame = ttk.Frame(frame)
treeFrame.grid(row=0, column=1, pady=10)

treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side='right', fill='y')



cols = ("Name", "Age", "Subscription", "Employment")
treeView = ttk.Treeview(treeFrame, yscrollcommand=treeScroll.set,show='headings', columns=cols, height=13 )

treeView.column("Name", width=100)
treeView.column("Age",width=50)
treeView.column("Subscription",width=100)
treeView.column("Employment",width=100)
treeView.pack()
treeScroll.config(command=treeView.yview)
load_data()


root.mainloop()