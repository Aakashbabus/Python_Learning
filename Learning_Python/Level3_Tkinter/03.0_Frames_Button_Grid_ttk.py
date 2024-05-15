# In Tkinter, a "Frame" is a container widget used to organize and group other widgets together
# within a window. Frames are like invisible boxes that you can place inside your main window or
# other frames to logically group related widgets or to organize the layout of your graphical user
# interface (GUI).

# ttk is themed tkinter , which is more advanced and make GUI look alike in Linux, Mac and Windows

import tkinter as tk
from tkinter import ttk

def on_button_click1():
    print("User Likes Green Color")
def on_button_click2():
    print("User Likes Blue Color")
# Create main window
root = tk.Tk()
root.title("Elegant GUI")
#root.geometry("500x700")
# Create a frame widget
frame = ttk.Frame(root, padding=20)

# Create a label widget
label = ttk.Label(frame, text="Which Color do you Like?", font=("Helvetica", 14))

# Create buttons widget
button1 = ttk.Button(frame, text="Blue", command=on_button_click1)
button2 = ttk.Button(frame, text="Green", command=on_button_click2)

# Configure grid ( Remember rows start with index 0 and column start with index 1 )
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

# adding the widgets to grid
frame.grid(row=0, column=0, sticky="nsew")
label.grid(row=0, column=0, columnspan=2, pady=10)
button1.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
button2.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Mainloop
root.mainloop()
