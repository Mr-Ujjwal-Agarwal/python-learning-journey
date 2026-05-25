# importing libraries
from tkinter import *
from time import strftime
import random
import math


# function to open window in center
def center_window(window, width, height):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x}+{y}")


# creating main window
root = Tk()

# title
root.title("MINI DESKTOP DASHBOARD")

# center dashboard
center_window(root, 900, 600)

# background color
root.config(bg="#dbeafe")


# ---------------- CALCULATOR ----------------

# calculator function
def calculator():

    calc = Toplevel(root)

    calc.title("Scientific Calculator")

    center_window(calc, 500, 650)

    calc.config(bg="#f8fafc")

    Label(
        calc,
        text="SCIENTIFIC CALCULATOR",
        font=("Arial", 22, "bold"),
        bg="#f8fafc",
        fg="#1e3a8a"
    ).grid(row=0, column=0, columnspan=5, pady=20)

    display = Entry(
        calc,
        font=("Arial", 25),
        justify="right",
        bd=5
    )

    display.grid(row=1, column=0, columnspan=5, padx=10, pady=20)


    # show values
    def show(value):

        display.insert(END, value)


    # clear display
    def clear():

        display.delete(0, END)


    # calculate answer
    def answer():

        result = eval(display.get())

        display.delete(0, END)

        display.insert(END, result)


    # scientific functions
    def sin_function():

        value = float(display.get())

        result = math.sin(math.radians(value))

        display.delete(0, END)

        display.insert(END, result)


    def cos_function():

        value = float(display.get())

        result = math.cos(math.radians(value))

        display.delete(0, END)

        display.insert(END, result)


    def tan_function():

        value = float(display.get())

        result = math.tan(math.radians(value))

        display.delete(0, END)

        display.insert(END, result)


    def asin_function():

        value = float(display.get())

        result = math.degrees(math.asin(value))

        display.delete(0, END)

        display.insert(END, result)


    def acos_function():

        value = float(display.get())

        result = math.degrees(math.acos(value))

        display.delete(0, END)

        display.insert(END, result)


    def atan_function():

        value = float(display.get())

        result = math.degrees(math.atan(value))

        display.delete(0, END)

        display.insert(END, result)


    button_color = "#2563eb"

    # scientific buttons
    Button(calc, text="sin", width=8, height=3, bg="purple", fg="white", command=sin_function).grid(row=2, column=0)

    Button(calc, text="cos", width=8, height=3, bg="purple", fg="white", command=cos_function).grid(row=2, column=1)

    Button(calc, text="tan", width=8, height=3, bg="purple", fg="white", command=tan_function).grid(row=2, column=2)

    Button(calc, text="asin", width=8, height=3, bg="purple", fg="white", command=asin_function).grid(row=2, column=3)

    Button(calc, text="acos", width=8, height=3, bg="purple", fg="white", command=acos_function).grid(row=2, column=4)

    Button(calc, text="atan", width=8, height=3, bg="purple", fg="white", command=atan_function).grid(row=3, column=0)

    # number buttons
    Button(calc, text="7", width=8, height=3, bg=button_color, fg="white", command=lambda: show("7")).grid(row=3, column=1)

    Button(calc, text="8", width=8, height=3, bg=button_color, fg="white", command=lambda: show("8")).grid(row=3, column=2)

    Button(calc, text="9", width=8, height=3, bg=button_color, fg="white", command=lambda: show("9")).grid(row=3, column=3)

    Button(calc, text="+", width=8, height=3, bg="green", fg="white", command=lambda: show("+")).grid(row=3, column=4)

    Button(calc, text="4", width=8, height=3, bg=button_color, fg="white", command=lambda: show("4")).grid(row=4, column=0)

    Button(calc, text="5", width=8, height=3, bg=button_color, fg="white", command=lambda: show("5")).grid(row=4, column=1)

    Button(calc, text="6", width=8, height=3, bg=button_color, fg="white", command=lambda: show("6")).grid(row=4, column=2)

    Button(calc, text="-", width=8, height=3, bg="green", fg="white", command=lambda: show("-")).grid(row=4, column=3)

    Button(calc, text="*", width=8, height=3, bg="green", fg="white", command=lambda: show("*")).grid(row=4, column=4)

    Button(calc, text="1", width=8, height=3, bg=button_color, fg="white", command=lambda: show("1")).grid(row=5, column=0)

    Button(calc, text="2", width=8, height=3, bg=button_color, fg="white", command=lambda: show("2")).grid(row=5, column=1)

    Button(calc, text="3", width=8, height=3, bg=button_color, fg="white", command=lambda: show("3")).grid(row=5, column=2)

    Button(calc, text="/", width=8, height=3, bg="green", fg="white", command=lambda: show("/")).grid(row=5, column=3)

    Button(calc, text="C", width=8, height=3, bg="red", fg="white", command=clear).grid(row=5, column=4)

    Button(calc, text="0", width=18, height=3, bg=button_color, fg="white", command=lambda: show("0")).grid(row=6, column=0, columnspan=2)

    Button(calc, text=".", width=8, height=3, bg=button_color, fg="white", command=lambda: show(".")).grid(row=6, column=2)

    Button(calc, text="=", width=18, height=3, bg="orange", fg="white", command=answer).grid(row=6, column=3, columnspan=2)


# ---------------- UNIT CONVERTER ----------------

def unit_conversion():

    converter = Toplevel(root)

    converter.title("Unit Converter")

    center_window(converter, 500, 500)

    converter.config(bg="#f8fafc")

    Label(
        converter,
        text="UNIT CONVERTER",
        font=("Arial", 22, "bold"),
        bg="#f8fafc",
        fg="#1e3a8a"
    ).pack(pady=20)

    value_entry = Entry(converter, font=("Arial", 18), width=20)

    value_entry.pack(pady=20)

    conversion_type = StringVar()

    conversion_type.set("Kilometer to Meter")


    # convert function
    def convert():

        value = float(value_entry.get())

        selected = conversion_type.get()

        if selected == "Kilometer to Meter":

            result = value * 1000

        elif selected == "KG to Gram":

            result = value * 1000

        elif selected == "Celsius to Fahrenheit":

            result = (value * 9/5) + 32

        result_label.config(text="Result : " + str(result))


    OptionMenu(
        converter,
        conversion_type,
        "Kilometer to Meter",
        "KG to Gram",
        "Celsius to Fahrenheit"
    ).pack(pady=20)

    Button(
        converter,
        text="Convert",
        width=18,
        height=2,
        bg="#2563eb",
        fg="white",
        command=convert
    ).pack(pady=20)

    result_label = Label(
        converter,
        text="Result : ",
        font=("Arial", 18),
        bg="#f8fafc"
    )

    result_label.pack(pady=20)

# ---------------- SECRET DIARY ----------------

# ---------------- SECRET DIARY ----------------

def secret_diary():

    diary = Toplevel(root)

    diary.title("Secret Diary")

    center_window(diary, 750, 700)

    diary.config(bg="#e0f2fe")


    # ---------------- CREATE PASSWORD ----------------

    def create_password():

        password = create_password_entry.get()

        file = open("password.txt", "w")

        file.write(password)

        file.close()

        status_label.config(
            text="Password Created Successfully ✔",
            fg="green"
        )


    # ---------------- LOGIN ----------------

    def login():

        entered_password = login_password_entry.get()

        file = open("password.txt", "r")

        saved_password = file.read()

        file.close()

        if entered_password == saved_password:

            status_label.config(
                text="Login Successful ✔",
                fg="green"
            )

            login_frame.pack_forget()

            note_box.pack(pady=20)

            button_frame.pack(pady=10)

        else:

            status_label.config(
                text="Wrong Password ✖",
                fg="red"
            )


    # ---------------- SAVE NOTES ----------------

    def save_notes():

        notes = note_box.get("1.0", END)

        file = open("diary.txt", "w")

        file.write(notes)

        file.close()

        status_label.config(
            text="Diary Saved Successfully ✔",
            fg="green"
        )


    # ---------------- OPEN NOTES ----------------

    def open_notes():

        file = open("diary.txt", "r")

        data = file.read()

        file.close()

        note_box.delete("1.0", END)

        note_box.insert(END, data)

        status_label.config(
            text="Diary Opened ✔",
            fg="green"
        )


    # ---------------- EDIT NOTES ----------------

    def edit_notes():

        note_box.config(state=NORMAL)

        status_label.config(
            text="Edit Mode Enabled ✏",
            fg="orange"
        )


    # ---------------- DELETE NOTES ----------------

    def delete_notes():

        note_box.delete("1.0", END)

        file = open("diary.txt", "w")

        file.write("")

        file.close()

        status_label.config(
            text="Diary Deleted ✖",
            fg="red"
        )


    # ---------------- NEW PAGE ----------------

    def new_page():

        note_box.delete("1.0", END)

        status_label.config(
            text="New Page Opened",
            fg="blue"
        )


    # ---------------- HEADING ----------------

    Label(
        diary,
        text="SECRET DIARY",
        font=("Arial", 26, "bold"),
        bg="#e0f2fe",
        fg="#1e3a8a"
    ).pack(pady=20)


    # ---------------- LOGIN FRAME ----------------

    login_frame = Frame(
        diary,
        bg="white",
        bd=3,
        relief=RIDGE
    )

    login_frame.pack(pady=20, padx=20, fill=X)


    # create password heading
    Label(
        login_frame,
        text="Create Password",
        font=("Arial", 14, "bold"),
        bg="white"
    ).pack(pady=10)


    # create password entry
    create_password_entry = Entry(
        login_frame,
        width=30,
        font=("Arial", 14),
        show="*"
    )

    create_password_entry.pack(pady=10)


    # create password button
    Button(
        login_frame,
        text="CREATE PASSWORD",
        width=20,
        height=2,
        bg="#2563eb",
        fg="white",
        font=("Arial", 10, "bold"),
        command=create_password
    ).pack(pady=10)


    # login heading
    Label(
        login_frame,
        text="Enter Password",
        font=("Arial", 14, "bold"),
        bg="white"
    ).pack(pady=10)


    # login password entry
    login_password_entry = Entry(
        login_frame,
        width=30,
        font=("Arial", 14),
        show="*"
    )

    login_password_entry.pack(pady=10)


    # login button
    Button(
        login_frame,
        text="LOGIN",
        width=20,
        height=2,
        bg="green",
        fg="white",
        font=("Arial", 10, "bold"),
        command=login
    ).pack(pady=10)


    # ---------------- NOTE BOX ----------------

    note_box = Text(
        diary,
        width=75,
        height=18,
        font=("Arial", 12),
        bd=4,
        relief=GROOVE
    )


    # ---------------- BUTTON FRAME ----------------

    button_frame = Frame(
        diary,
        bg="#e0f2fe"
    )


    Button(
        button_frame,
        text="SAVE NOTES",
        width=15,
        height=2,
        bg="#2563eb",
        fg="white",
        font=("Arial", 10, "bold"),
        command=save_notes
    ).grid(row=0, column=0, padx=10, pady=10)


    Button(
        button_frame,
        text="OPEN NOTES",
        width=15,
        height=2,
        bg="#2563eb",
        fg="white",
        font=("Arial", 10, "bold"),
        command=open_notes
    ).grid(row=0, column=1, padx=10, pady=10)


    Button(
        button_frame,
        text="EDIT NOTES",
        width=15,
        height=2,
        bg="orange",
        fg="white",
        font=("Arial", 10, "bold"),
        command=edit_notes
    ).grid(row=1, column=0, padx=10, pady=10)


    Button(
        button_frame,
        text="NEW PAGE",
        width=15,
        height=2,
        bg="#0ea5e9",
        fg="white",
        font=("Arial", 10, "bold"),
        command=new_page
    ).grid(row=1, column=1, padx=10, pady=10)


    Button(
        button_frame,
        text="DELETE NOTES",
        width=15,
        height=2,
        bg="red",
        fg="white",
        font=("Arial", 10, "bold"),
        command=delete_notes
    ).grid(row=2, column=0, columnspan=2, pady=10)


    # ---------------- STATUS LABEL ----------------

    status_label = Label(
        diary,
        text="",
        font=("Arial", 12, "bold"),
        bg="#e0f2fe"
    )

    status_label.pack(pady=15)


 


  
 
   

   


  
   
    


# ---------------- GUESSING GAME ----------------

# guessing game function
def game():

    game_window = Toplevel(root)

    game_window.title("Guessing Game")

    center_window(game_window, 400, 400)

    game_window.config(bg="#f8fafc")

    secret_number = random.randint(100, 999)

    attempts = 0


    # check guess
    def check():

        nonlocal attempts

        guess = int(entry.get())

        attempts = attempts + 1

        if guess > secret_number:

            result.config(text="Too High")

        elif guess < secret_number:

            result.config(text="Too Low")

        else:

            result.config(text="You Won In " + str(attempts) + " Attempts")


    Label(game_window, text="GUESSING GAME", font=("Arial", 22, "bold"), bg="#f8fafc", fg="#1e3a8a").pack(pady=20)

    Label(game_window, text="Guess A 3 Digit Number", font=("Arial", 14), bg="#f8fafc").pack()

    entry = Entry(game_window, font=("Arial", 20))

    entry.pack(pady=20)

    Button(game_window, text="Check", width=15, bg="#2563eb", fg="white", command=check).pack()

    result = Label(game_window, text="", font=("Arial", 16), bg="#f8fafc")

    result.pack(pady=20)


# ---------------- DIGITAL CLOCK ----------------

# clock function
def clock():

    clock_window = Toplevel(root)

    clock_window.title("Digital Clock")

    center_window(clock_window, 400, 200)

    # update clock
    def update_time():

        current_time = strftime('%H:%M:%S %p')

        label.config(text=current_time)

        label.after(1000, update_time)


    label = Label(clock_window, font=("Arial", 40, "bold"), bg="black", fg="white")

    label.pack(fill=BOTH, expand=1)

    update_time()


# ---------------- PASSWORD GENERATOR ----------------

# password generator function
def password():

    pass_window = Toplevel(root)

    pass_window.title("Password Generator")

    center_window(pass_window, 400, 300)

    pass_window.config(bg="#f8fafc")


    # generate password
    def generate():

        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%"

        password = ""

        length = int(length_entry.get())

        for i in range(length):

            password = password + random.choice(chars)

        result.config(text=password)


    Label(pass_window, text="PASSWORD GENERATOR", font=("Arial", 20, "bold"), bg="#f8fafc", fg="#1e3a8a").pack(pady=20)

    Label(pass_window, text="Enter Password Length", font=("Arial", 14), bg="#f8fafc").pack()

    length_entry = Entry(pass_window)

    length_entry.pack(pady=10)

    Button(pass_window, text="Generate Password", width=20, bg="#2563eb", fg="white", command=generate).pack(pady=20)

    result = Label(pass_window, text="", font=("Arial", 16), bg="#f8fafc")

    result.pack()


# ---------------- TO DO LIST ----------------

# to do list function
def to_do_list():

    todo = Toplevel(root)

    todo.title("To Do List")

    center_window(todo, 500, 500)

    todo.config(bg="#f8fafc")


    # add task function
    def add_task():

        task = task_entry.get()

        listbox.insert(END, task)

        task_entry.delete(0, END)


    # delete selected task
    def delete_task():

        selected_task = listbox.curselection()

        listbox.delete(selected_task)


    # save tasks
    def save_tasks():

        tasks = listbox.get(0, END)

        file = open("tasks.txt", "w")

        for task in tasks:

            file.write(task + "\n")

        file.close()

        status_label.config(text="Tasks Saved")


    # open saved tasks
    def open_tasks():

        listbox.delete(0, END)

        file = open("tasks.txt", "r")

        tasks = file.readlines()

        file.close()

        for task in tasks:

            listbox.insert(END, task.strip())

        status_label.config(text="Tasks Opened")


    # clear tasks
    def clear_tasks():

        listbox.delete(0, END)

        status_label.config(text="All Tasks Cleared")


    Label(todo, text="TO DO LIST", font=("Arial", 24, "bold"), bg="#f8fafc", fg="#1e3a8a").pack(pady=20)

    task_entry = Entry(todo, width=35, font=("Arial", 14))

    task_entry.pack(pady=10)

    Button(todo, text="ADD TASK", width=18, height=2, bg="#2563eb", fg="white", command=add_task).pack(pady=5)

    listbox = Listbox(todo, width=45, height=12, font=("Arial", 12))

    listbox.pack(pady=20)

    Button(todo, text="DELETE TASK", width=18, height=2, bg="red", fg="white", command=delete_task).pack(pady=5)

    Button(todo, text="SAVE TASKS", width=18, height=2, bg="#2563eb", fg="white", command=save_tasks).pack(pady=5)

    Button(todo, text="OPEN TASKS", width=18, height=2, bg="green", fg="white", command=open_tasks).pack(pady=5)

    Button(todo, text="CLEAR ALL", width=18, height=2, bg="orange", fg="white", command=clear_tasks).pack(pady=5)

    status_label = Label(todo, text="", font=("Arial", 12, "bold"), bg="#f8fafc", fg="green")

    status_label.pack(pady=15)


# ---------------- EXIT FUNCTION ----------------

# exit function
def exit_the_app():

    root.destroy()


# ---------------- DASHBOARD HEADING ----------------

Label(root, text="MINI DESKTOP DASHBOARD", font=("Arial", 28, "bold"), bg="#dbeafe", fg="#1e3a8a").grid(row=0, column=0, columnspan=2, pady=30)


# ---------------- DASHBOARD BUTTONS ----------------

Button(root, text="CALCULATOR", width=20, height=3, bg="#2563eb", fg="white", font=("Arial", 12, "bold"), command=calculator).grid(row=1, column=0, padx=25, pady=20)

Button(root, text="UNIT CONVERTER", width=20, height=3, bg="#2563eb", fg="white", font=("Arial", 12, "bold"), command=unit_conversion).grid(row=1, column=1, padx=25, pady=20)

Button(root, text="SECRET DIARY", width=20, height=3, bg="#2563eb", fg="white", font=("Arial", 12, "bold"), command=secret_diary).grid(row=2, column=0, padx=25, pady=20)

Button(root, text="GUESSING GAME", width=20, height=3, bg="#2563eb", fg="white", font=("Arial", 12, "bold"), command=game).grid(row=2, column=1, padx=25, pady=20)

Button(root, text="DIGITAL CLOCK", width=20, height=3, bg="#2563eb", fg="white", font=("Arial", 12, "bold"), command=clock).grid(row=3, column=0, padx=25, pady=20)

Button(root, text="TO DO LIST", width=20, height=3, bg="#2563eb", fg="white", font=("Arial", 12, "bold"), command=to_do_list).grid(row=3, column=1, padx=25, pady=20)

Button(root, text="PASSWORD GENERATOR", width=20, height=3, bg="#2563eb", fg="white", font=("Arial", 12, "bold"), command=password).grid(row=4, column=0, padx=25, pady=20)

Button(root, text="EXIT", width=20, height=3, bg="red", fg="white", font=("Arial", 12, "bold"), command=exit_the_app).grid(row=4, column=1, padx=25, pady=20)


# running dashboard
root.mainloop()
