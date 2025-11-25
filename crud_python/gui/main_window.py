import tkinter as tk
from tkinter import ttk
from gui.create_user import CreateUserWindow
from gui.delete_user import DeleteUserWindow
from db import Database

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema CRUD")
        self.db = Database()

        # Botón Crear Usuario
        ttk.Button(
            root,
            text="Crear Usuario",
            command=self.open_create_user
        ).pack(pady=10)

        # Botón Eliminar Usuario
        ttk.Button(
            root,
            text="Eliminar Usuario",
            command=self.open_delete_user
        ).pack(pady=10)

    # Abrir ventana de creación
    def open_create_user(self):
        CreateUserWindow(self.root, self.db)

    # Abrir ventana de eliminación
    def open_delete_user(self):
        DeleteUserWindow(self.root, self.db)
        ttk.Button(root, text="Crear Usuario",
                   command=self.open_create_user).pack(pady=10)

    def open_create_user(self):
        CreateUserWindow(self.root, self.db)
