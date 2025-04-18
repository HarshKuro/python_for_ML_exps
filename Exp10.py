#create a window in tkinter, from tkinter import *, crete a calculator using tkinter, use loops, Set the size of the calculator
from tkinter import *
def button_click(number):
    current = equation.get()
    equation.set(current + str(number))

def calculate():
    try:
        result = eval(equation.get())
        equation.set(result)
    except Exception as e:
        equation.set("Error")

def clear():
    equation.set("")

root = Tk()
root.title("Calculator")
root.geometry("400x600")
root.resizable(0, 0)
root.configure(background="grey")

equation = StringVar()
entry = Entry(root, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify='center')
entry.grid(row=0, column=0, columnspan=4)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
    ]
row_val = 1
col_val = 0
for button in buttons:
    if button == "=":
        btn = Button(root, text=button, padx=1, pady=30, font=('Arial', 18), bg="lightblue", command=calculate)
    elif button == "C":
        btn = Button(root, text=button, padx=30, pady=30, font=('Arial', 18), bg="lightcoral", command=clear)
    else:
        btn = Button(root, text=button, padx=30, pady=30, font=('Arial', 18), bg="lightgray", command=lambda b=button: button_click(b))
    
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()  # Move this to the end