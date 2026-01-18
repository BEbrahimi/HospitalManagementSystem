import random
import tkinter as tk
from tkinter import ttk, messagebox

from HMS.db.databaseConnection import get_connection

def add_patients(
    app_id_ent, patient_name_ent,dob_ent,time_ent, dep_var, doctor_var, email_ent,phone_ent, msg_txt,status_var
):
    id = app_id_ent.get()
    patient_name = patient_name_ent.get()
    dob = dob_ent.get()
    time = time_ent.get()
    dept = dep_var.get()
    doctor = doctor_var.get()
    email = email_ent.get()
    phone = phone_ent.get()
    msg_txt = msg_txt.get("1.0", "end-1c")
    status = status_var.get()



    if not patient_name or not email or not doctor or not phone:
        messagebox.showerror("Error", "All fields are required")
        return
    try:
        con = get_connection()
        cur = con.cursor()
        # ➕ insert Doctor
        add_appointment = """
                INSERT INTO appointment (id, patient_name, dob, time, department, doctor, email, phone, message, status)
                VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s)
                """
        values = (id,patient_name,dob,time,dept,doctor,email,phone,msg_txt,status)
        cur.execute(add_appointment, values)
        con.commit()

        messagebox.showinfo("Success", "Registration Successful")

        cur.close()
        con.close()
    except Exception as e:
        messagebox.showerror("Database Error", str(e))





def get_active_doctors():
    try:
        con = get_connection()
        cur = con.cursor()

        query = """
        SELECT full_name
        FROM doctors
        WHERE status = %s
          AND full_name IS NOT NULL
          AND full_name != ''
        ORDER BY full_name
        """
        cur.execute(query, ('Active',))

        doctors = [row[0] for row in cur.fetchall()]
        return doctors

    except Exception as e:
        print("DB Error:", e)
        return []

    finally:
        con.close()

def add_appointment_form(content_frame):

    container = tk.Frame(content_frame, bg="white")
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
    def generate_appointment_id():
        number = random.randint(1, 9999)
        return f"APT-{number:04d}"

    # =========================
    # BASIC INFO
    # =========================
    create_label("Appointment ID", 1, 0, True)
    create_label("Patient Name", 1, 2)

    app_id_ent = create_entry(2, 0, 2)

    # Generate and insert ID
    app_id_ent.insert(0, generate_appointment_id())
    app_id_ent.config(
        state='readonly',
        readonlybackground='#e0e0e0',
        fg='black'
    )
    patient_name_ent = create_entry(2, 2, 2)


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
        values=get_active_doctors(),
        style="Custom.TCombobox"
    )
    doctor_cb.grid(row=6, column=2,columnspan=2, sticky="we", padx=10, ipady=4)


    # =========================
    # PHONE & AVATAR
    # =========================
    create_label("Email", 7, 0)
    email_ent = create_entry(8, 0, 2)

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
        command= lambda:add_patients(
    app_id_ent, patient_name_ent,dob_ent,time_ent, dep_var, doctor_var, email_ent,phone_ent, msg_txt,status_var
)
    ).grid(row=13, column=0, columnspan=4, pady=30)
