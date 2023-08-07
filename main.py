from tkinter import *
from tkinter.font import Font
import math as m


def digict_to_number(number):
    global flag_is_dot
    if (entry_display.get() == "0." and flag_is_dot == 0) or entry_display.get() == "ERROR: division by zero":
        entry_display.delete(0, END)
    current = entry_display.get()
    entry_display.delete(0, END)

    if len(current) > 0 and current[-1] == '.' and flag_is_dot == 0:
        current = current[:-1]
        entry_display.insert(0, str(current) + str(number) + ".")
    elif not '.' in current:
        entry_display.insert(0, str(current) + str(number) + ".")
    else:
        entry_display.insert(0, str(current) + str(number))


def clear():
    entry_display.delete(0, END)
    entry_display.insert(0, "0.")
    global flag_is_dot
    flag_is_dot = 0
    global f_num
    f_num = 0
    global math
    math = "-"


def add():
    first_number = entry_display.get()
    if first_number == "":
        return
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    entry_display.delete(0, END)
    global flag_is_dot
    flag_is_dot = 0


def equal():
    second_number = entry_display.get()
    if second_number == "":
        return
    entry_display.delete(0, END)
    if math == "addition":
        entry_display.insert(0, str(float(f_num) + float(second_number)))
    elif math == "subtraction":
        entry_display.insert(0, str(float(f_num) - float(second_number)))
    elif math == "multiplication":
        entry_display.insert(0, str(float(f_num) * float(second_number)))
    elif math == "division":
        if float(second_number) == 0:
            entry_display.insert(0, "ERROR: division by zero")
        else:
            entry_display.insert(0, str(float(f_num) / float(second_number)))
    else:
        entry_display.insert(0, "0.")
    global flag_is_dot
    flag_is_dot = 0


def substract():
    first_number = entry_display.get()
    if first_number == "":
        return
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    entry_display.delete(0, END)
    global flag_is_dot
    flag_is_dot = 0


def multiply():
    first_number = entry_display.get()
    if first_number == "":
        return
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    entry_display.delete(0, END)
    global flag_is_dot
    flag_is_dot = 0


def divide():
    first_number = entry_display.get()
    if first_number == "":
        return
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    entry_display.delete(0, END)
    entry_display.insert(0, "0.")
    global flag_is_dot
    flag_is_dot = 0


def element():
    current = entry_display.get()
    entry_display.delete(0, END)
    num = float(current)
    num = m.sqrt(num)
    entry_display.insert(0, str(num))


def dot():
    global flag_is_dot
    flag_is_dot = 1


def change_sign():
    current = entry_display.get()
    entry_display.delete(0, END)
    num = float(current) * (-1)
    entry_display.insert(0, str(num))


def on_entry_key_press(event):
    # Blokuj wprowadzanie danych ręcznie
    return "break"
if __name__ == "__main__":
    root = Tk()
    root.title("Calculator")
    root.iconbitmap("icon.ico")
    root.configure(bg="#3D3D3D")
    bold_font = Font(size=16, weight='bold')
    entry_display = Entry(root
                          , width=32, borderwidth=5, background="#9EC49E", relief=SUNKEN, justify="right",
                          font=bold_font)
    entry_display.grid(padx=10, pady=10, columnspan=5)
    entry_display.insert(0, "0.")
    entry_display.bind("<KeyPress>", on_entry_key_press)

    # Define variables
    global flag_is_dot
    flag_is_dot = 0
    global f_num
    f_num = 0
    global math
    math = "-"
    # Define Buttons
    button1 = Button(root, text="1", padx=20, pady=10, background="#686868", fg="white", font=bold_font,
                     command=lambda: digict_to_number(1))
    button2 = Button(root, text="2", padx=20, pady=10, background="#686868", fg="white", font=bold_font,
                     command=lambda: digict_to_number(2))
    button3 = Button(root, text="3", padx=20, pady=10, background="#686868", fg="white", font=bold_font,
                     command=lambda: digict_to_number(3))
    button4 = Button(root, text="4", padx=20, pady=10, background="#686868", fg="white", font=bold_font,
                     command=lambda: digict_to_number(4))
    button5 = Button(root, text="5", padx=20, pady=10, background="#686868", fg="white", font=bold_font,
                     command=lambda: digict_to_number(5))
    button6 = Button(root, text="6", padx=20, pady=10, background="#686868", fg="white", font=bold_font,
                     command=lambda: digict_to_number(6))
    button7 = Button(root, text="7", padx=20, pady=10, background="#686868", fg="white", font=bold_font,
                     command=lambda: digict_to_number(7))
    button8 = Button(root, text="8", padx=20, pady=10, background="#686868", fg="white", font=bold_font,
                     command=lambda: digict_to_number(8))
    button9 = Button(root, text="9", padx=20, pady=10, background="#686868", fg="white", font=bold_font,
                     command=lambda: digict_to_number(9))
    button0 = Button(root, text="0", padx=20, pady=10, background="#686868", fg="white", font=bold_font,
                     command=lambda: digict_to_number(0))

    button_element = Button(root, text="√", padx=20, pady=10, background="#686868", fg="white",
                            font=bold_font, command=element)
    button_clear = Button(root, text="C", padx=19, pady=9, background="#686868", fg="white", font=bold_font,
                          command=clear)
    button_equal = Button(root, text="=", padx=20, pady=10, background="#686868", fg="white", font=bold_font,
                          command=equal)
    button_sign_change = Button(root, text="±", padx=20, pady=10, background="#686868", fg="white",
                                font=bold_font, command=change_sign)
    button_multiplication = Button(root, text="×", padx=20, pady=10, background="#686868", fg="white", font=bold_font,
                                   command=multiply)
    button_division = Button(root, text="÷", padx=20, pady=10, background="#686868", fg="white", font=bold_font,
                             command=divide)
    button_addition = Button(root, text="+", padx=20, pady=45, background="#686868", fg="white", font=bold_font,
                             command=add)
    button_subtraction = Button(root, text="-", padx=22, pady=10, background="#686868", fg="white", font=bold_font,
                                command=substract)
    button_dot = Button(root, text=".", padx=22, pady=10, background="#686868", fg="white",
                        font=bold_font, command=dot)

    # Put the buttons on the screen
    button7.grid(row=1, column=0, pady=5, padx=5)
    button8.grid(row=1, column=1, pady=5, padx=5)
    button9.grid(row=1, column=2, pady=5, padx=5)
    button_element.grid(row=1, column=3, pady=5, padx=5)
    button_clear.grid(row=1, column=4, pady=5, padx=5)

    button4.grid(row=2, column=0, pady=5, padx=5)
    button5.grid(row=2, column=1, pady=5, padx=5)
    button6.grid(row=2, column=2, pady=5, padx=5)
    button_sign_change.grid(row=2, column=3, pady=5, padx=5)
    button_division.grid(row=2, column=4, pady=5, padx=5)

    button1.grid(row=3, column=0, pady=5, padx=5)
    button2.grid(row=3, column=1, pady=5, padx=5)
    button3.grid(row=3, column=2, pady=5, padx=5)
    button_multiplication.grid(row=3, column=4, pady=5, padx=5)

    button_addition.grid(row=3, column=3, pady=5, padx=2, rowspan=5)

    button0.grid(row=4, column=0, pady=5, padx=5)
    button_dot.grid(row=4, column=1, pady=5, padx=5)
    button_equal.grid(row=4, column=2, pady=5, padx=5)
    button_subtraction.grid(row=4, column=4, pady=5, padx=5)

    root.mainloop()
