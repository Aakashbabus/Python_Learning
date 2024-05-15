import tkinter as tk

window = tk.Tk()

# Basic Configurations
window.title("Aakash")
window.geometry("500x700")
window.config(bg="white")

# Adding a label with attributes
label = tk.Label(window, text="Hello World", bg="white", foreground="Black")
label.pack()

# Mainloop
window.mainloop()
