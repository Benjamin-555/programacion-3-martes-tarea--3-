import tkinter as tk
from tkinter import ttk, messagebox

class UpdateUserWindow:
    def __init__(self, root, db):
        self.db = db

        self.win = tk.Toplevel(root)
        self.win.title("Editar Usuario")
        self.win.geometry("450x350")
        self.win.resizable(False, False)

        ttk.Label(
            self.win,
            text="Seleccione un usuario",
            font=("Segoe UI", 11, "bold")
        ).pack(pady=10)

        # Tabla
        self.table = ttk.Treeview(
            self.win,
            columns=("id", "name", "email"),
            show="headings"
        )
        self.table.heading("id", text="ID")
        self.table.heading("name", text="Nombre")
        self.table.heading("email", text="Email")
        self.table.pack(padx=10, pady=5, fill="both", expand=True)

        ttk.Button(
            self.win,
            text="Editar Seleccionado",
            command=self.load_user_data
        ).pack(pady=10)

        # Campos
        form = ttk.Frame(self.win)
        form.pack(pady=5)

        ttk.Label(form, text="Nombre:").grid(row=0, column=0, pady=5, padx=5)
        ttk.Label(form, text="Email:").grid(row=1, column=0, pady=5, padx=5)

        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()

        ttk.Entry(form, textvariable=self.name_var).grid(row=0, column=1)
        ttk.Entry(form, textvariable=self.email_var).grid(row=1, column=1)

        ttk.Button(
            self.win,
            text="Guardar Cambios",
            command=self.save_changes
        ).pack(pady=10)

        self.load_data()
        self.selected_id = None

    def load_data(self):
        # Limpiar tabla
        for item in self.table.get_children():
            self.table.delete(item)

        users = self.db.get_users()
        for u in users:
            self.table.insert("", tk.END, values=u)

    def load_user_data(self):
        selected = self.table.selection()
        if not selected:
            messagebox.showwarning("Atención", "Debe seleccionar un usuario")
            return

        values = self.table.item(selected[0])["values"]
        self.selected_id = values[0]

        self.name_var.set(values[1])
        self.email_var.set(values[2])

    def save_changes(self):
        if not self.selected_id:
            messagebox.showwarning("Error", "Seleccione un usuario primero")
            return

        name = self.name_var.get()
        email = self.email_var.get()

        if not name or not email:
            messagebox.showwarning("Atención", "Todos los campos son obligatorios")
            return

        self.db.update_user(self.selected_id, name, email)
        self.load_data()
        messagebox.showinfo("Éxito", "Usuario actualizado correctamente")
      
