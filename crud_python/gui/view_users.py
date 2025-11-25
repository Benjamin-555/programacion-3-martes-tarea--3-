import tkinter as tk
from tkinter import ttk

class ViewUsersWindow:
    def __init__(self, root, db):
        self.db = db

        self.window = tk.Toplevel(root)
        self.window.title("Lista de Usuarios")

        # Tabla
        self.tree = ttk.Treeview(
            self.window,
            columns=("ID", "Nombre", "Email"),
            show="headings"
        )
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Email", text="Email")
        self.tree.pack(fill="both", expand=True)

        self.load_users()

    def load_users(self):
        users = self.db.get_users()
        for user in users:
            self.tree.insert("", tk.END, values=user)
