from multiprocessing.sharedctypes import Value
from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter.scrolledtext import ScrolledText
from typing import Type
import names
from tkinter import messagebox

root  = tk.Tk()
root.geometry('400x600')
root.title("Name Generators")


def search():

        Gender = gender.get()
        Type = types.get()  


        if Gender == 'Male' and Type == "Full Name":
                name = names.get_full_name(gender="male")
                try:
                        text.insert('end',' ')
                        if text.get in int:
                                raise(Exception)
                except(Exception):
                        messagebox.showwarning('warning',"Jangan Angka")
                text.insert('end',name)
                
        elif Gender == 'Male' and Type == "First Name":
                name = names.get_first_name()
                try:
                        text.insert('end',' ')
                        if text.get in int:
                                raise(Exception)
                except(Exception):
                        messagebox.showwarning('warning',"Jangan Angka")
                text.insert('end',name)
                
        elif Gender == 'Male' and Type == "Last Name":
                name = names.get_last_name()
                try:
                        text.insert('end',' ')
                        if text.get in int:
                                raise(Exception)
                except(Exception):
                        messagebox.showwarning('warning',"Jangan Angka")
                text.insert('end',name)
                
        elif Gender == 'Female' and Type == "Full Name":
                name = names.get_full_name(gender="female")
                try:
                        text.insert('end',' ')
                        if text.get in int:
                                raise(Exception)
                except(Exception):
                        messagebox.showwarning('warning',"Jangan Angka")
                text.insert('end',name)
                
        elif Gender == 'Female' and Type == "First Name":
                name = names.get_first_name()
                try:
                        text.insert('end',' ')
                        if text.get in int:
                                raise Exception("Jangan Angka")
                except:
                        messagebox.showwarning('warning',"Jangan Angka")
                text.insert('end',name)
                
        elif Gender == 'Female' and Type == "Last Name":
                name = names.get_last_name()
                try:
                        text.insert('end',' ')
                        if text.get in int:
                                raise(Exception)
                except(Exception):
                        messagebox.showwarning('warning',"Jangan Angka")
                text.insert('end',name)
                

for i in range (0,100):
 l2 =  Label(root, text="Name Generators",font=('verdana',15,'bold'),bg="black",fg="white")
l2.place(x=110,y=10)

l1 = Label(root,text="Gender",font=('verdana',10,'bold'))
l1.place(x=10,y=60)
g = tk.StringVar() 
gender = Combobox(root, width = 13, textvariable = g, state='readonly',font=('verdana',10,'bold'),) 
gender['values'] = ('Male', 'Female')
gender.place(x=10,y=90)
gender.current(0) 

l2 = Label(root,text="Type",font=('verdana',10,'bold'))
l2.place(x=170,y=60)
t = tk.StringVar() 
types = Combobox(root, width = 13, textvariable = t, state='readonly',font=('verdana',10,'bold'),) 
types['values'] = ('Full Name', 'First Name','Last Name')
types.place(x=170,y=90)
types.current(0) 


button = Button(root,text="Search",font=('verdana','10','bold'),command=search)
button.place(x=320,y=85)


text = ScrolledText(root,width=40,height=3)
text['font'] = ("verdana",10,'bold')
text.place(x=10,y=130)



root.mainloop()
