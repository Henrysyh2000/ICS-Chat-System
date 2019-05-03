# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:37:39 2019

@author: Henry
"""

import tkinter as tk

#create window
window = tk.Tk()
window.title('Welcome to SRH Chat System!')
window.geometry('500x500')

#icon
canvas = tk.Canvas(window, height=256, width=256)
image_file = tk.PhotoImage(file='icon.png')
image = canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack(side='top')

#label
label1 = tk.Label(window, text='User name:', font=('Arial Bold', 18),
                  width=15, height=1)
label2 = tk.Label(window, text='Password:', font=('Arial Bold', 18),
                  width=15, height=1)
label1.place(x=30, y=300,anchor='w')
label2.place(x=29, y=350,anchor='w')

#Entry
e1 = tk.Entry(window, show=None, font=('Arial', 16), width=15)
e2 = tk.Entry(window, show='*',font=('Arial', 16), width=15)
e1.place(x=250, y=303, anchor='w')
e2.place(x=250, y=353, anchor='w')

#login and register function
def login():
    pass
def register():
    pass
#button
b1 = tk.Button(window, text='Login',
               font=('Arial Bold', 12), bg='green', fg='white',
               width=10, height=2,
               command=login)
b2 = tk.Button(window, text='Register', bg='grey', fg='white',
               font=('Arial Bold', 12), 
               width=10, height=2, 
               command=register)

b1.place(x=120, y=420, anchor='w')
b2.place(x=270, y=420, anchor='w')

window.mainloop()
