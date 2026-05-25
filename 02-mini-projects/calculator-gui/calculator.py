from tkinter import *


root = Tk()
root.title("My Calculator")
root.geometry("1000x1000")


display = Entry(root, width=20, font=("Arial", 20))

display.grid(row=0, column=0, columnspan=3, padx=10, pady=20)



def seven():
    display.insert(END, "7")


def eight():
    display.insert(END, "8")


def nine():
    display.insert(END, "9")

def one():
    display.insert(END, "1")


def two():
    display.insert(END, "2")


def three():
    display.insert(END, "3")

def four():
    display.insert(END, "4")


def five():
    display.insert(END, "5")


def six():
    display.insert(END, "6")


def plus():
    display.insert(END, "+")

def minus():
    display.insert(END, "-")

def mul():
    display.insert(END, "*")

def div():
    display.insert(END, "/")

def percentange():
    display.insert(END, "%")

def backspace():
    current = display.get()
    display.delete(0, END)
    display.insert(0, current[:-1])

def zero():
    display.insert(END, "0")

def double_zero():
    display.insert(END, "00")

def point():
    display.insert(END, ".")


def equal():
    result = eval(display.get())
    display.delete(0, END)
    display.insert(0, result)


def clear():
    display.delete(0, END)


Button(root, text="7", width=10, height=2, command=seven).grid(row=2, column=0)

Button(root, text="8", width=10, height=2, command=eight).grid(row=2, column=1)

Button(root, text="9", width=10, height=2, command=nine).grid(row=2, column=2)

Button(root, text="4", width=10, height=2, command=four).grid(row=3, column=0)

Button(root, text="5", width=10, height=2, command=five).grid(row=3, column=1)

Button(root, text="6", width=10, height=2, command=six).grid(row=3, column=2)

Button(root, text="1", width=10, height=2, command=one).grid(row=4, column=0)

Button(root, text="2", width=10, height=2, command=two).grid(row=4, column=1)

Button(root, text="3", width=10, height=2, command=three).grid(row=4, column=2)

Button(root, text="0", width=10, height=2, command=zero).grid(row=5, column=1)

Button(root, text="00", width=10, height=2, command=double_zero).grid(row=5, column=0)

Button(root, text="+", width=10, height=2, command=plus).grid(row=4, column=3)

Button(root, text="-", width=10, height=2, command=minus).grid(row=3, column=3)

Button(root, text="*", width=10, height=2, command=mul).grid(row=2, column=3)

Button(root, text="/", width=10, height=2, command=div).grid(row=1, column=3)

Button(root, text="%", width=10, height=2, command=percentange).grid(row=1, column=1)

Button(root, text=".", width=10, height=2, command=point).grid(row=5, column=2)

Button(root, text="⌫", width=10, height=2, command=backspace).grid(row=1, column=2)

Button(root, text="=", width=10, height=2, command=equal).grid(row=5, column=3)

Button(root, text="C", width=10, height=2, command=clear).grid(row=1, column=0)

root.mainloop()
