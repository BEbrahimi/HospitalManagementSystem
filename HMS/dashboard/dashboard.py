import os
import tkinter as tk
from PIL import Image, ImageTk

from HMS.dashboard.appointments import create_upcoming_appointments
from HMS.dashboard.doctors import create_doctors_section


def dashboard_items(content_frame):

    # ---------- Card Frame ----------
    card = tk.Frame(
        content_frame,
        bg="white",
        width=230,
        height=120,
        highlightthickness=1,
        highlightbackground="#e0e0e0"
    )
    card.place(x=20, y=20)
    card.pack_propagate(False)

    # ---------- Load Doctor Icon ----------
    current_dir = os.path.dirname(__file__)  # HMS/dashboard
    base_dir = os.path.dirname(current_dir)  # HMS
    icon_path = os.path.join(base_dir, "icon", "doctor_icon.png")

    img = Image.open(icon_path)
    img = img.resize((60, 60))
    doctor_icon = ImageTk.PhotoImage(img)

    icon_label = tk.Label(card, image=doctor_icon,bg="#Fff")
    icon_label.image = doctor_icon
    icon_label.place(x=20, y=30)

    # ---------- Count ----------
    tk.Label(
        card,
        text="98",
        font=("Segoe UI", 22, "bold"),
        fg="#555",
        bg="white"
    ).place(x=170, y=20)

    # ---------- Doctors Button ----------
    tk.Label(
        card,
        text=" Doctors ✓ ",
        font=("Segoe UI", 10, "bold"),
        fg="white",
        bg="#0d6efd",
        padx=10,
        pady=3
    ).place(x=110, y=65)

    # ---------- patients Frame ----------
    patients = tk.Frame(
        content_frame,
        bg="white",
        width=230,
        height=120,
        highlightthickness=1,
        highlightbackground="#e0e0e0"
    )
    patients.place(x=310, y=20)
    patients.pack_propagate(False)

    # ---------- Load Doctor Icon ----------
    current_dir = os.path.dirname(__file__)  # HMS/dashboard
    base_dir = os.path.dirname(current_dir)  # HMS
    icon_path = os.path.join(base_dir, "icon", "dashboardColor.png")

    img = Image.open(icon_path)
    img = img.resize((60, 60))
    doctor_icon = ImageTk.PhotoImage(img)

    icon_label = tk.Label(patients, image=doctor_icon, bg="#Fff")
    icon_label.image = doctor_icon
    icon_label.place(x=20, y=30)

    # ---------- Count ----------
    tk.Label(
        patients,
        text="98",
        font=("Segoe UI", 22, "bold"),
        fg="#555",
        bg="white"
    ).place(x=170, y=20)

    # ---------- Doctors Button ----------
    tk.Label(
        patients,
        text=" Patients ✓ ",
        font=("Segoe UI", 10, "bold"),
        fg="white",
        bg="#55ce63",
        padx=10,
        pady=3
    ).place(x=110, y=65)

    # ---------- attend Frame ----------
    attend = tk.Frame(
        content_frame,
        bg="white",
        width=230,
        height=120,
        highlightthickness=1,
        highlightbackground="#e0e0e0"
    )
    attend.place(x=600, y=20)
    attend.pack_propagate(False)

    # ---------- Load Doctor Icon ----------
    current_dir = os.path.dirname(__file__)  # HMS/dashboard
    base_dir = os.path.dirname(current_dir)  # HMS
    icon_path = os.path.join(base_dir, "icon", "dashboardColor.png")

    img = Image.open(icon_path)
    img = img.resize((60, 60))
    doctor_icon = ImageTk.PhotoImage(img)

    icon_label = tk.Label(attend, image=doctor_icon, bg="#Fff")
    icon_label.image = doctor_icon
    icon_label.place(x=20, y=30)

    # ---------- Count ----------
    tk.Label(
        attend,
        text="98",
        font=("Segoe UI", 22, "bold"),
        fg="#555",
        bg="white"
    ).place(x=170, y=20)

    # ---------- Doctors Button ----------
    tk.Label(
        attend,
        text=" Attend ✓ ",
        font=("Segoe UI", 10, "bold"),
        fg="white",
        bg="#7a92a3",
        padx=10,
        pady=3
    ).place(x=110, y=65)

    # ---------- pending Frame ----------
    pending = tk.Frame(
        content_frame,
        bg="white",
        width=230,
        height=120,
        highlightthickness=1,
        highlightbackground="#e0e0e0"
    )
    pending.place(x=900, y=20)
    pending.pack_propagate(False)

    # ---------- Load Doctor Icon ----------
    current_dir = os.path.dirname(__file__)  # HMS/dashboard
    base_dir = os.path.dirname(current_dir)  # HMS
    icon_path = os.path.join(base_dir, "icon", "dashboardColor.png")

    img = Image.open(icon_path)
    img = img.resize((60, 60))
    doctor_icon = ImageTk.PhotoImage(img)

    icon_label = tk.Label(pending, image=doctor_icon, bg="#Fff")
    icon_label.image = doctor_icon
    icon_label.place(x=20, y=30)

    # ---------- Count ----------
    tk.Label(
        pending,
        text="98",
        font=("Segoe UI", 22, "bold"),
        fg="#555",
        bg="white"
    ).place(x=170, y=20)

    # ---------- Doctors Button ----------
    tk.Label(
        pending,
        text=" Pending ✓ ",
        font=("Segoe UI", 10, "bold"),
        fg="white",
        bg="#ffbc35",
        padx=10,
        pady=3
    ).place(x=110, y=65)

    #upcoming appointments
    appointment = tk.Frame(
        content_frame,
        bg="#fff",
        width=750,
        height=400,
        highlightthickness=1,
        highlightbackground="#e0e0e0"
    )
    appointment.place(x=20, y=170)
    appointment.pack_propagate(False)
    create_upcoming_appointments(appointment)
    # Doctor's appointments
    pending = tk.Frame(
        content_frame,
        bg="#fff",
        width=350,
        height=400,
        highlightthickness=1,
        highlightbackground="#e0e0e0"
    )
    pending.place(x=780, y=170)
    pending.pack_propagate(False)
    create_doctors_section(pending)



