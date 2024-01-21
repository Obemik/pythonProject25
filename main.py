import tkinter
from tkinter import *

root = Tk()

root.config(bg="#86F4FF")
root.title("Hello world!")
root.geometry('500x600+900+300')

# btn1 = Button(root, text="Hello 1",  bg="pink")
# btn2 = Button(root, text="Hello 2",  bg="pink")
# btn3 = Button(root, text="Hello 3",  bg="pink")
# btn4 = Button(root, text="Hello world",  bg="pink")
# btn5 = Button(root, text="Hello 5",  bg="pink")
# btn6 = Button(root, text="Hello 6",  bg="pink")
# btn7 = Button(root, text="Hello 7",  bg="pink")
# btn8 = Button(root, text="Hello 8",  bg="pink")
# btn1.grid(row = 1, column= 0)
# btn2.grid(row = 1, column= 1, stick="w")
# btn3.grid(row = 2, column= 0)
# btn4.grid(row = 2, column= 1)
# btn5.grid(row = 3, column= 0)
# btn6.grid(row = 3, column= 1, stick="e")
# btn7.grid(row = 4, column= 0, columnspan=2, stick="we")
# btn8.grid(row = 1, column= 2, rowspan= 4, stick="ns")
# root.grid_columnconfigure (0, minsize=200)
# root.grid_columnconfigure(1, minsize=100)

def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print("Empty")

def del_entry():
    name.delete(0, END)

label = Label(root, text="Ім'я", bg="#86F4FF", fg="black", )
label.grid(row=0, column=0, sticky="w")

label2 = Label(root, text="Пароль", bg="#86F4FF", fg="black", )
label2.grid(row=1, column=0, sticky="w")

name = Entry(root)
name.grid(row=0, column=1, sticky="w")

name2 = Entry(root)
name2.grid(row=1, column=1, sticky="w")

btn1 = Button(root, text="Ввести",command= get_entry, bg="pink").grid(row=2, column=0, stick="we")
btn2 = Button(root, text="Видалити",command= del_entry, bg="pink").grid(row=2, column=1, stick="we")


root.grid_columnconfigure(0, minsize=200)
root.grid_columnconfigure(1, minsize=100)

root.mainloop()
