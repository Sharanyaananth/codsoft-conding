import tkinter as tk

def button_click(n):
    cur= entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, cur + n)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

w= tk.Tk()
w.title(" My Calculator")


entry = tk.Entry(w, width=60)
entry.grid(row=0, column=0, columnspan=4)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(w, text=button, width=10, command=lambda b=button: button_click(b) if b != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


tk.Button(w, text='clear', width=10, command=clear).grid(row=row_val, column=col_val)


w.mainloop()