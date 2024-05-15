# When you run this program, it will open a window displaying "Hello World". The tkinter library provides
# a variety of widgets and options for creating graphical user interfaces (GUIs) in Python.
# In this example, we used a Label widget to display the text "Hello World".

import tkinter as tk

# Create the main application window
root = tk.Tk()

# Create a label widget with "Hello World" text
label = tk.Label(root, text="Hello World")
    
# Pack the label widget to make it visible in the window
label.pack()

# Start the Tkinter event loop
root.mainloop()
