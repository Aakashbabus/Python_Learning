import tkinter as tk

def draw_circle(event):
    x = event.x
    y = event.y
    canvas.create_oval(x-20, y-20, x+20, y+20, fill="blue")

def draw_rectangle(event):
    x = event.x
    y = event.y
    canvas.create_rectangle(x-20, y-20, x+20, y+20, fill="red")

# Create the main window
root = tk.Tk()
root.title("Drawing Shapes")

# Create a Canvas widget
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Bind left mouse click to draw a circle
canvas.bind("<Button-3>", draw_circle)

# Bind right mouse click to draw a rectangle
canvas.bind("<Button-1>", draw_rectangle)

# Run the Tkinter event loop
root.mainloop()
