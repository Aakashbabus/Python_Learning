import tkinter as tk

def hello():
    print("Hello!")

# Create main window
root = tk.Tk()
root.title("Menu Example")

# Create a menu
menu_bar = tk.Menu(root)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=hello)
file_menu.add_command(label="Save", command=hello)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create an "Edit" menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=hello)
edit_menu.add_command(label="Copy", command=hello)
edit_menu.add_command(label="Paste", command=hello)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Create a "Help" menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=hello)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Configure root window to use the menu
root.config(menu=menu_bar)

root.mainloop()