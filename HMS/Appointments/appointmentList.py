import os
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from HMS.db.databaseConnection import get_connection


def select_patients():
    try:
        con = get_connection()
        cur = con.cursor()

        query = """
        SELECT first_name, date_of_birth, address,phone,email
        FROM patients
        ORDER BY id DESC
        """
        cur.execute(query)

        data = cur.fetchall()

        cur.close()
        con.close()

        return data

    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return []




def appointment_list(content_frame):

    # =========================
    # SAMPLE DATA
    # =========================
    data = select_patients()

    # =========================
    # VARIABLES
    # =========================
    entries_var = tk.IntVar(value=10)
    current_page = tk.IntVar(value=1)

    # =========================
    # STYLE
    # =========================
    style = ttk.Style()
    style.theme_use("default")

    style.configure(
        "Treeview",
        background="#ffffff",
        foreground="#333333",
        rowheight=46,
        fieldbackground="#ffffff",
        font=("Segoe UI", 10)
    )

    style.configure(
        "Treeview.Heading",
        font=("Segoe UI", 11, "bold"),
        background="#f1f3f6",
        foreground="#000000"
    )

    style.map(
        "Treeview",
        background=[("selected", "#e3f2fd")]
    )

    # =========================
    # TOP BAR
    # =========================
    top_frame = tk.Frame(content_frame, bg="#ffffff")
    top_frame.pack(fill="x", padx=20, pady=12)

    tk.Label(
        top_frame,
        text="Show",
        bg="#ffffff",
        font=("Segoe UI", 11)
    ).pack(side="left")

    entries_box = ttk.Combobox(
        top_frame,
        textvariable=entries_var,
        values=[10, 20, 50],
        width=7,
        font=("Segoe UI", 11),
        state="readonly"
    )
    entries_box.pack(side="left", padx=8)

    tk.Label(
        top_frame,
        text="entries",
        bg="#ffffff",
        font=("Segoe UI", 11)
    ).pack(side="left")

    # =========================
    # TABLE FRAME
    # =========================
    table_frame = tk.Frame(content_frame, bg="#ffffff")
    table_frame.pack(fill="both", expand=True, padx=20)

    columns = ("Appointment ID", "Patient Name", "Age", "Doctor Name", "Department", "Date", "Time","Status","Action")

    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="tree headings",
        height=10
    )

    # Column widths
    tree.column("#0", width=1, anchor="center")   # Avatar
    tree.heading("#0",)

    tree.column("Appointment ID", width=120)
    tree.column("Patient Name", width=140, anchor="center")
    tree.column("Age", width=50,anchor="center")
    tree.column("Doctor Name", width=140,anchor="center")
    tree.column("Department", width=140,anchor="center")
    tree.column("Date", width=100,anchor="center")
    tree.column("Time", width=100,anchor="center")
    tree.column("Status", width=100,anchor="center")
    tree.column("Action", width=100, anchor="center")

    for col in columns:
        tree.heading(col, text=col)

    tree.pack(side="left", fill="both", expand=True)

    # =========================
    # SCROLLBAR
    # =========================
    scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=tree.yview
    )
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")




