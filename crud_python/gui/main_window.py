import tkinter as tk
from tkinter import ttk
from gui.create_user import CreateUserWindow
from gui.delete_user import DeleteUserWindow
from gui.update_user import UpdateUserWindow
from gui.view_users import ViewUsersWindow
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

        # Botón Actualizar Usuario
        ttk.Button(
            root,
            text="Actualizar Usuario",
            command=self.open_update_user
        ).pack(pady=10)

        # Botón Ver Usuarios
        ttk.Button(
            root,
            text="Ver Usuarios",
            command=self.open_view_users
        ).pack(pady=10)

    def open_create_user(self):
        CreateUserWindow(self.root, self.db)

    def open_delete_user(self):
        DeleteUserWindow(self.root, self.db)

    def open_update_user(self):
        UpdateUserWindow(self.root, self.db)

    def open_view_users(self):
        ViewUsersWindow(self.root, self.db)

