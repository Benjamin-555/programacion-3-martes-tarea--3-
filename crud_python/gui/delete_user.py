import tkinter as tk
from tkinter import ttk, messagebox

class DeleteUserWindow:
    def __init__(self, root, db):
        self.db = db

        self.win = tk.Toplevel(root)
        self.win.title("Eliminar Usuario")
        self.win.geometry("450x300")
        self.win.resizable(False, False)

        ttk.Label(
            self.win,
            text="Usuarios Registrados",
            font=("Segoe UI", 12, "bold")
        ).pack(pady=10)

        # Tabla de usuarios
        self.table = ttk.Treeview(
            self.win,
            columns=("id", "name", "email"),
            show="headings"
        )
        self.table.heading("id", text="ID")
        self.table.heading("name", text="Nombre")
        self.table.heading("email", text="Email")
        self.table.pack(fill="both", expand=True, padx=10)

        # Botón eliminar
        ttk.Button(
            self.win,
            text="Eliminar Seleccionado",
            command=self.delete_selected
        ).pack(pady=10)

        # Cargar datos al abrir
        self.load_data()

    def load_data(self):
        # Limpia la tabla
        for row in self.table.get_children():
            self.table.delete(row)

        # Carga los usuarios desde la DB
        users = self.db.get_users()
        for user in users:
            self.table.insert("", tk.END, values=user)

    def delete_selected(self):
        selected = self.table.selection()

        # Validación
        if not selected:
            messagebox.showwarning("Atención", "Debe seleccionar un usuario.")
            return

        user_values = self.table.item(selected[0])["values"]
        user_id = user_values[0]

        # Confirmación
        if not messagebox.askyesno("Confirmar", f"¿Eliminar usuario con ID {user_id}?"):
            return

        # Eliminar
        self.db.delete_user(user_id)

        # Recargar tabla
        self.load_data()

        messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
      
