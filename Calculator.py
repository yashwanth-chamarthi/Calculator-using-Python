import tkinter
from typing import Sized

cal = tkinter.Tk()
cal.geometry("265x370")
cal.title("Calculator")

expression = ""

# define functions
def add_char(value):
    global expression
    expression += value
    label_result.config(text = expression)

def clear():
    global expression
    expression = ""
    label_result.config(text = expression)

def calculate():
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)
            expression = str(result)
        except:
            result = 'error'
            expression = ""
    label_result.config(text = result)

# define GUI
label_result = tkinter.Label(cal, text = "",)
label_result.grid(row=0,column=0, columnspan=4)
label_result.config(font=100)

label_1 = tkinter.Button(cal, text = "1",height=4,width=8, command= lambda: add_char("1"))
label_1.grid(row=1,column=0)

label_2 = tkinter.Button(cal, text = "2",height=4,width=8, command= lambda: add_char("2"))
label_2.grid(row=1,column=1)

label_3 = tkinter.Button(cal, text = "3",height=4,width=8, command= lambda: add_char("3"))
label_3.grid(row=1,column=2)

label_divide = tkinter.Button(cal, text = "/",height=4,width=8, command= lambda: add_char("/"))
label_divide.grid(row=1,column=3)

label_4 = tkinter.Button(cal, text = "4",height=4,width=8, command= lambda: add_char("4"))
label_4.grid(row=2,column=0)

label_5 = tkinter.Button(cal, text = "5",height=4,width=8, command= lambda: add_char("5"))
label_5.grid(row=2,column=1)

label_6 = tkinter.Button(cal, text = "6",height=4,width=8, command= lambda: add_char("6"))
label_6.grid(row=2,column=2)

label_multiply = tkinter.Button(cal, text = "*",height=4,width=8, command= lambda: add_char("*"))
label_multiply.grid(row=2,column=3)

label_7 = tkinter.Button(cal, text = "7",height=4,width=8, command= lambda: add_char("7"))
label_7.grid(row=3,column=0)

label_8 = tkinter.Button(cal, text = "8",height=4,width=8, command= lambda: add_char("8"))
label_8.grid(row=3,column=1)

label_9 = tkinter.Button(cal, text = "9",height=4,width=8, command= lambda: add_char("9"))
label_9.grid(row=3,column=2)

label_subtract = tkinter.Button(cal, text = "-",height=4,width=8, command= lambda: add_char("-"))
label_subtract.grid(row=3,column=3)

label_clear = tkinter.Button(cal, text = "C",height=4,width=8, command= lambda: clear())
label_clear.grid(row=4,column=0)

label_0 = tkinter.Button(cal, text = "0",height=4,width=8, command= lambda: add_char("0"))
label_0.grid(row=4,column=1)

label_dot = tkinter.Button(cal, text = ".",height=4,width=8, command= lambda: add_char("."))
label_dot.grid(row=4,column=2)

label_addition = tkinter.Button(cal, text = "+",height=4,width=8, command= lambda: add_char("+"))
label_addition.grid(row=4,column=3)

label_calculate= tkinter.Button(cal, text = "=",height=3,width = 36, command= lambda: calculate())
label_calculate.grid(row=5,column=0, columnspan=4)

cal.mainloop()