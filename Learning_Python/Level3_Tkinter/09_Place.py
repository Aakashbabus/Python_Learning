import tkinter as tk

def move_label():
    # Move the label to a new position
    label.place(x=50, y=100)

# Create the main window
root = tk.Tk()
root.geometry("300x200")  # Set the size of the window

# Create a label widget
label = tk.Label(root, text="This is a label")

# Place the label in the initial position
label.place(x=100, y=50)

# Create a button to move the label
button = tk.Button(root, text="Move Label", command=move_label)
button.place(x=120, y=150)

# Start the Tkinter event loop
root.mainloop()
