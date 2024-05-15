import tkinter as tk

def click_button(character):
    current_text = entry_field.get()
    entry_field.delete(0, tk.END)
    entry_field.insert(tk.END, current_text + character)

def clear():
    entry_field.delete(0, tk.END)

def calculate():
    expression = entry_field.get()
    try:
        result = eval(expression)
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, str(result))
    except Exception as e:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

entry_field = tk.Entry(root, width=20, font=("Arial", 14))
entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 1
col = 0
for button in buttons:
    if button == "=":
        tk.Button(root, text=button, width=5, command=calculate).grid(row=row, column=col)
    elif button == "C":
        tk.Button(root, text=button, width=5, command=clear).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, width=5, command=lambda char=button: click_button(char)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
