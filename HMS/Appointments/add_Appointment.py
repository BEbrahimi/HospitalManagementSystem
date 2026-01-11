import os
import random
import shutil
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import bcrypt
from HMS.db.databaseConnection import get_connection

def scrollable_frame(parent):
    canvas = tk.Canvas(
        parent,
        bg="white",
        highlightthickness=0
    )

    scrollbar = tk.Scrollbar(
        parent,
        orient="vertical",
        command=canvas.yview
    )

    scroll_frame = tk.Frame(canvas, bg="white")

    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window(
        (0, 0),
        window=scroll_frame,
        anchor="nw"
    )

    canvas.configure(yscrollcommand=scrollbar.set)

    #  padding
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    return scroll_frame

def add_appointment_form(content_frame):
    form_area = scrollable_frame(content_frame)

    container = tk.Frame(form_area, bg="white")
    container.pack(fill="both", expand=True, padx=20)

    container.grid_columnconfigure(0, weight=1, uniform="x")
    container.grid_columnconfigure(1, weight=1, uniform="x")
    container.grid_columnconfigure(2, weight=1, uniform="x")
    container.grid_columnconfigure(3, weight=1, uniform="x")



    # ================= Title =================
    tk.Label(
        container,
        text="Add Appointment",
        bg="white",
        fg="#333",
        font=("Segoe UI", 18, "bold")
    ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(10, 20))
    # =========================
    # VARIABLES
    # =========================
    status_var = tk.StringVar(value="Active")
    dep_var = tk.StringVar()
    doctor_var = tk.StringVar()


    # =========================
    # GRID CONFIG
    # =========================
    for i in range(4):
        container.columnconfigure(i, weight=1, uniform="x")

    # =========================
    # HELPERS
    # =========================
    def create_label(text, row, col, required=False):
        tk.Label(
            container,
            text=text + (" *" if required else ""),
            bg="white",
            fg="#444",
            font=("Segoe UI", 10)
        ).grid(row=row, column=col, sticky="w", pady=(8, 4), padx=10)

    def create_entry(row, col, colspan=1, show=None):
        ent = tk.Entry(
            container,
            font=("Segoe UI", 10),
            relief="solid",
            bd=1
        )
        if show:
            ent.config(show=show)

        ent.grid(
            row=row,
            column=col,
            columnspan=colspan,
            sticky="we",
            padx=10,
            ipady=6
        )
        return ent

    def shorten_filename(name, max_len=30):
        return name if len(name) <= max_len else name[:max_len - 3] + "..."

    def generate_appointment_id():
        number = random.randint(1, 9999)
        return f"APT-{number:04d}"

    # =========================
    # BASIC INFO
    # =========================
    create_label("Appointment ID", 1, 0, True)
    create_label("Patient Name", 1, 2)

    app_id_ent = create_entry(2, 0, 2)
    patient_name_ent = create_entry(2, 2, 2)
    # Generate and insert ID
    app_id_ent.insert(0, generate_appointment_id())

    # =========================
    # DATE & GENDER
    # =========================
    create_label("Date of Birth", 3, 0)
    create_label("Time", 3, 2)

    dob_ent = create_entry(4, 0, 2)
    time_ent = create_entry(4, 2, 2)


    # =========================
    # LOCATION
    # =========================
    create_label("Department", 5, 0)
    create_label("Doctor", 5, 2)
    style = ttk.Style()
    style.configure("Custom.TCombobox", padding=6)

    dep_cb = ttk.Combobox(
        container,
        textvariable=dep_var,
        values=["Dentists", "Neurology", "Ophthalmology", "Orthopedics", "Cancer Department"],
        style="Custom.TCombobox"
    )
    dep_cb.grid(row=6, column=0,columnspan=2, sticky="we", padx=10, ipady=4)


    doctor_cb = ttk.Combobox(
        container,
        textvariable=doctor_var,
        values=["Dentists", "Neurology", "Ophthalmology", "Orthopedics","Cancer Department" ,"ENT Department"],
        style="Custom.TCombobox"
    )
    doctor_cb.grid(row=6, column=2,columnspan=2, sticky="we", padx=10, ipady=4)


    # =========================
    # PHONE & AVATAR
    # =========================
    create_label("Email", 7, 0)
    phone_ent = create_entry(8, 0, 2)

    create_label("Phone", 7, 2)
    phone_ent = create_entry(8, 2, 2)

    # =========================
    # BIOGRAPHY
    # =========================
    create_label("Message", 9, 0)

    msg_txt = tk.Text(
        container,
        height=4,
        font=("Segoe UI", 10),
        relief="solid",
        bd=1
    )
    msg_txt.grid(row=10, column=0, columnspan=4, sticky="we", padx=10, pady=(0, 10))

    # =========================
    # STATUS
    # =========================
    create_label("Appointment Status", 11, 0)

    tk.Radiobutton(
        container, text="Active",
        variable=status_var, value="Active",
        bg="white"
    ).grid(row=12, column=0, sticky="w", padx=10)

    tk.Radiobutton(
        container, text="Inactive",
        variable=status_var, value="Inactive",
        bg="white"
    ).grid(row=12, column=1, sticky="w", padx=10)

    # =========================
    # SUBMIT
    # =========================
    tk.Button(
        container,
        text="CREATE APPOINTMENT",
        bg="#0d6efd",
        fg="white",
        font=("Segoe UI", 11, "bold"),
        relief="flat",
        padx=30,
        pady=10,
        cursor="hand2",
    ).grid(row=13, column=0, columnspan=4, pady=30)
