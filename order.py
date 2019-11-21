import tkinter
from tkinter import *

root = tkinter.Tk()
root.title('Order Up!')
root.geometry('500x500')

select=None

head = Label(root, text='Order your Food')
head.grid(row = 0, column = 3, sticky=E)

fd1 = Checkbutton(root, text = 'Biryani')
fd1.grid(row = 1, column = 0, sticky=W)

fd1 = Checkbutton(root, text = 'Fried Rice')
fd1.grid(row = 2, column = 0, sticky=W)

fd1 = Checkbutton(root, text = 'Palak Paneer')
fd1.grid(row = 3, column = 0, sticky=W)

fd1 = Checkbutton(root, text = 'Chocolate Ice Cream')
fd1.grid(row = 4, column = 0, sticky=W)

root.mainloop()
