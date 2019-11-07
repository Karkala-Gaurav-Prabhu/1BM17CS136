from tkinter import *

root = Tk()
root.title("Movie Booking Application")
root.geometry("310x300")
m = Label(root, text='Lets Go For A Movie')
m.grid(row=0, column=2)

v = IntVar()
EngMovies = ["Intersteller","Jumanji","Up","Conjuring","Annabelle"]

eng = Radiobutton(root, text='English', variable = v, value = 'english')
eng.grid(row = 1, sticky=W)
tel = Radiobutton(root, text='Telugu', variable = v, value = 'telugu')
tel.grid(row = 2, sticky=W)
tam = Radiobutton(root, text='Tamil', variable = v, value = 'tamil')
tam.grid(row = 3, sticky=W)
kan = Radiobutton(root, text='Kannada', variable = v, value = 'kannada')
kan.grid(row = 4, sticky=W)

for movie in EngMovies:
    Checkbutton(root, text = movie, )

root.mainloop()
