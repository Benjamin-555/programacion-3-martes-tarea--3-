import tkinter as tk
from tkinter import ttk
from gui.create_user import CreateUserWindow
from db import Database

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema CRUD")
        self.db = Database()

        ttk.Button(root, text="Crear Usuario",
                   command=self.open_create_user).pack(pady=10)

    def open_create_user(self):
        CreateUserWindow(self.root, self.db)
