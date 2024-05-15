import tkinter as tk

def show_selection():
    if var1.get() == 1:
        label.config(text="Aakash selected")
    else:
        label.config(text="Aakash deselected")

    if var2.get() == 1:
        label2.config(text="Atharva selected")
    else:
        label2.config(text="Atharva 2 deselected")

# Create the main window
root = tk.Tk()
root.title("Checkbox Example")

# Create IntVar objects to track the state of the checkboxes
var1 = tk.IntVar()
var2 = tk.IntVar()

# Create Checkbutton widgets
checkbox1 = tk.Checkbutton(root, text="Aakash", variable=var1, command=show_selection)
checkbox1.pack()

checkbox2 = tk.Checkbutton(root, text="Atharva", variable=var2, command=show_selection)
checkbox2.pack()

# Create labels to display the selection status
label = tk.Label(root, text="")
label.pack()

label2 = tk.Label(root, text="")
label2.pack()

# Run the Tkinter event loop
root.mainloop()
