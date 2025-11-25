import tkinter as tk
from tkinter import ttk

class CreateUserWindow:
    def __init__(self, root, db):
        self.db = db

        self.win = tk.Toplevel(root)
        self.win.title("Crear Usuario")

        ttk.Label(self.win, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.win, text="Email:").grid(row=1, column=0, padx=5, pady=5)

        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()

        ttk.Entry(self.win, textvariable=self.name_var).grid(row=0, column=1)
        ttk.Entry(self.win, textvariable=self.email_var).grid(row=1, column=1)

        ttk.Button(self.win, text="Guardar", command=self.save_user).grid(
            row=2, column=0, columnspan=2, pady=10)

    def save_user(self):
        name = self.name_var.get()
        email = self.email_var.get()

        print(f"Se guardaría: {name} - {email}")
import tkinter as tk
from tkinter import ttk

class CreateUserWindow:
    def __init__(self, root, db):
        self.db = db

        self.win = tk.Toplevel(root)
        self.win.title("Crear Usuario")

        ttk.Label(self.win, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.win, text="Email:").grid(row=1, column=0, padx=5, pady=5)

        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()

        ttk.Entry(self.win, textvariable=self.name_var).grid(row=0, column=1)
        ttk.Entry(self.win, textvariable=self.email_var).grid(row=1, column=1)

        ttk.Button(self.win, text="Guardar", command=self.save_user).grid(
            row=2, column=0, columnspan=2, pady=10)

    def save_user(self):
        name = self.name_var.get()
        email = self.email_var.get()

        print(f"Se guardaría: {name} - {email}")
