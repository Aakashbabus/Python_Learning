import tkinter as tk
import tkinter.messagebox


def show_message_box():

    question = tkinter.messagebox.askokcancel("Weather", "Will it Rain Today?")

    if question is True:
        tkinter.messagebox.showinfo("Message Box", "Test Message, Please Close the Window")


# Create the main window
root = tk.Tk()
root.title("Message Box Example")

# Create a button to display the message box
button = tk.Button(root, text="Show Message Box", command=show_message_box)
button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
