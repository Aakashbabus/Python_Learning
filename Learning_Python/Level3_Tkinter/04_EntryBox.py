import tkinter as tk
from tkinter import ttk


def on_button_click():
    print("User is Trying to Sign In")

    # get the data from the entry widgets
    entry_text_user = e1.get()
    entry_text_pw = e2.get()

    # clear the data in the entry widgets
    e1.delete(0, "end")
    e2.delete(0, "end")

    # process the data fedin by the user
    if entry_text_user == "guest" and entry_text_pw == "guest":
        print("Login Successful")

    else:
        print("invalid Credentials/ User Doesn't exist ")


# Create main window
root = tk.Tk()
root.title("Login Screen")

# Creating widgets
frame = ttk.Frame(root, padding=20)
label2 = ttk.Label(frame, text="E-mail", font=("Helvetica", 14))
label3 = ttk.Label(frame, text="Password", font=("Helvetica", 14))
e1 = ttk.Entry(frame, width=30)
e2 = ttk.Entry(frame, width=30, show="*")
button1 = ttk.Button(frame, text="Sign-in", command=on_button_click)

# define the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

# adding widgets to grid
frame.grid(row=0, column=0, sticky="nsew")
label2.grid(row=0, column=0, pady=10)  # Placed in a separate column
label3.grid(row=1, column=0, pady=10)
e1.grid(row=0, column=1, pady=10)
e2.grid(row=1, column=1, pady=10)
button1.grid(row=2, column=1, padx=5, pady=5)

# Mainloop
root.mainloop()
