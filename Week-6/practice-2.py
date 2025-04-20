import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
def welcomeMessage(root, username):
    window = tk.Toplevel(root)
    window.title("Admin Box")
    window.geometry("500x200")

    label_1 = tk.Label(window, text = f"Welcome {username}\n")
    label_1.pack()
    label_2 = tk.Label(window, text = "This is Python GUI with Tkinter")
    label_2.pack()

def submit(root, username_entry=None, password_entry=None):
    username = username_entry.get()
    password = password_entry.get()

    if username == "Mary" and password == "cos102":
        welcomeMessage(root, username)
    else:
        messagebox.showerror("Login", "Invalid username or password")
root = tk.Tk()
root.title("Login")
root.geometry("500x200")

tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show='*')
password_entry.pack()

tk.Button(root, text="Login", command=lambda: submit(root, username_entry, password_entry)).pack(pady=10)
root.mainloop()

