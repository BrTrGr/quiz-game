from tkinter import *
import random
import string

# def random_number():
#     random_num1 = random.randint(0,9)
#     lab.config(text=random_num1)

# def random_letter():
#     random_num2 = random.choice(string.ascii_letters)
#     lab.config(text=random_num2)

# def square():
#     x = editor.get()
#     lab.config(text=int(x)**2)


# window = Tk()
# window.geometry("800x800")

# lab = Label(window, font="Arial, 30", text="Put number")

# but1 = Button(window, command=random_number, font="Arial, 30", text="Bruno", width=15, height=4, bg="black", fg="yellow")
# but2 = Button(window, command=random_letter, font="Arial, 30", text="Triano", width=15, height=4, bg="black", fg="yellow")
# but3 = Button(window, command=square, font="Arial, 30", text="Triano", width=15, height=4, bg="black", fg="yellow")

# lab.pack()
# editor.pack()

# but1.pack()

# lab.pack()
# but1.pack()
# but2.pack()

# window.mainloop()

# from tkinter import *

def func():
    lab.config(text='Press')

window = Tk()
window.geometry("600x400")
lab = Label(window, font="Arial, 30", text="1")
but1 = Button(window, font="Arial, 30", text="Bruno", width=20, height=5, bg="black", fg="yellow")
but1.bind("<Button-1>", func())
lab.pack()
but1.pack()
window.mainloop()