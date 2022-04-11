
from tkinter import *
import tkinter as tk
from turtle import title
import hashlib

hasha = hashlib.new('whirlpool')

def read_input_field_1a2():
    loginname = input_field_1.get()
    passwordin = input_field_2.get()
    pwb = bytes(passwordin, "utf-8")
    hasha.update(pwb)
    print(loginname, " ", hasha.hexdigest())

window = tk.Tk()
window.title('Satan 3D')
window.minsize(width=800,height=400)
window.configure(background='green')

input_field_1 = Entry(window)
input_field_2 = Entry(window)
ok_button = Button(window, text='Login', command=read_input_field_1a2)

login_label = tk.Label(text="Username: ")
pw_label = tk.Label(text="Password: ")

login_label.pack()
input_field_1.pack()
pw_label.pack()
input_field_2.pack()
ok_button.pack()

login_label.place(relx=0.01, rely=0.01)
pw_label.place(relx=0.01, rely=0.075)
input_field_1.place(relx= 0.1, rely=0.01)
input_field_2.place(relx= 0.1, rely=0.08)
ok_button.place(relx=0.205,rely=0.15)

window.mainloop()

input()