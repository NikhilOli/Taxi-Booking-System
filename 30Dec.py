import tkinter as tk
from tkinter import ttk, messagebox

import sqlite3

class CRUDApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD Application")

        # Database
        self.conn = sqlite3.connect("crud.db")
        self.cursor = self.conn.cursor()

        # Create table if not exists
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS records
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT, age INTEGER, email TEXT)''')
        self.conn.commit()

        # GUI Components
        self.label_name = tk.Label(root, text="Name:")
        self.label_name.grid(row=0, column=0, padx=10, pady=10)
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_age = tk.Label(root, text="Age:")
        self.label_age.grid(row=1, column=0, padx=10, pady=10)
        self.entry_age = tk.Entry(root)
        self.entry_age.grid(row=1, column=1, padx=10, pady=10)

        self.label_email = tk.Label(root, text="Email:")
        self.label_email.grid(row=2, column=0, padx=10, pady=10)
        self.entry_email = tk.Entry(root)
        self.entry_email.grid(row=2, column=1, padx=10, pady=10)

        # Treeview
        self.tree = ttk.Treeview(root, columns=("ID", "Name", "Age", "Email"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Email", text="Email")
        self.tree.grid(row=4, columnspan=4, padx=10, pady=10)

        # Buttons
        self.btn_create = tk.Button(root, text="Create", command=self.create_record)
        self.btn_create.grid(row=3, column=0, padx=10, pady=10)

        self.btn_read = tk.Button(root, text="Read", command=self.read_records)
        self.btn_read.grid(row=3, column=1, padx=10, pady=10)

        self.btn_update = tk.Button(root, text="Update", command=self.update_record)
        self.btn_update.grid(row=3, column=2, padx=10, pady=10)

        self.btn_delete = tk.Button(root, text="Delete", command=self.delete_record)
        self.btn_delete.grid(row=3, column=3, padx=10, pady=10)

        # Display Area
        self.display_area = tk.Text(root, height=10, width=40)
        self.display_area.grid(row=5, columnspan=4, padx=10, pady=10)

    def create_record(self):
        name = self.entry_name.get()
        age = self.entry_age.get()
        email = self.entry_email.get()

        if name and age and email:
            self.cursor.execute('''INSERT INTO records (name, age, email) VALUES (?, ?, ?)''', (name, age, email))
            self.conn.commit()
            messagebox.showinfo("Success", "Record created successfully!")
            self.clear_entries()
            self.read_records()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def read_records(self):
        self.tree.delete(*self.tree.get_children())

        self.cursor.execute('''SELECT * FROM records''')
        records = self.cursor.fetchall()

        if records:
            for record in records:
                self.tree.insert("", "end", values=record)

        else:
            messagebox.showinfo("No Records", "No records found.")

    def update_record(self):
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showerror("Error", "Please select a record to update.")
            return

        selected_id = self.tree.item(selected_item, "values")[0]
        name = self.entry_name.get()
        age = self.entry_age.get()
        email = self.entry_email.get()

        self.cursor.execute('''UPDATE records SET name=?, age=?, email=? WHERE id=?''', (name, age, email, selected_id))
        self.conn.commit()
        messagebox.showinfo("Success", "Record updated successfully!")
        self.clear_entries()
        self.read_records()

    def delete_record(self):
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showerror("Error", "Please select a record to delete.")
            return

        selected_id = self.tree.item(selected_item, "values")[0]

        self.cursor.execute('''DELETE FROM records WHERE id=?''', (selected_id,))
        self.conn.commit()
        messagebox.showinfo("Success", "Record deleted successfully!")
        self.clear_entries()
        self.read_records()

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDApplication(root)
    root.mainloop()
