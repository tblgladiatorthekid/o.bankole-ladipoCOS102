import tkinter as tk
from tkinter import messagebox
def button_click(msgbox):
    msgbox.showinfo("Info", "Welcome to COS 102 GUI App!\n")
    result = msgbox.askyesno("Confirmation", "Do you want ot continue?\n")

root = tk.Tk()
root.title("Homepage")
root.geometry("300x100")

label = tk.Label(root, text="Hello friend \n")
label.pack()

button = tk.Button(root, text = "Click Me!", command = button_click)
button.pack()

button.config(fg = "red", bg = "yellow")

root.mainloop()