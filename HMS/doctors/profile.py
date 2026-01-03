import os
import tkinter as tk
from tkinter import messagebox

from PIL import Image, ImageTk

from HMS.db.databaseConnection import get_connection


def doctors_profile(doctor_id,content_frame):
    con = get_connection()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM doctors WHERE id=%s", (doctor_id,))
    doctor = cur.fetchone()
    cur.close()
    con.close()

    if not doctor:
        messagebox.showerror("Error", "Doctor not found")
        return
    content_frame.configure(bg="#f5f7fa")

    # ===================== MAIN CARD =====================
    main_card = tk.Frame(content_frame, bg="white", bd=0, relief="solid")
    main_card.pack(fill="x", padx=30, pady=30)

    # ===================== TOP SECTION =====================
    top = tk.Frame(main_card, bg="white")
    top.pack(fill="x", padx=25, pady=20)

    # ---------- LEFT (IMAGE + BASIC INFO) ----------
    left = tk.Frame(top, bg="white")
    left.pack(side="left", fill="y")

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    IMAGE_DIR = os.path.join(BASE_DIR, "image")
    image_name = doctor["image"]
    image_path = os.path.join(IMAGE_DIR, image_name)

    if not os.path.exists(image_path):
        image_path = os.path.join(IMAGE_DIR, "user.jpg")

    img = Image.open(image_path).resize((120, 120))
    photo = ImageTk.PhotoImage(img)

    avatar = tk.Label(left, image=photo, bg="white")
    avatar.image = photo
    avatar.pack(side="left")

    tk.Label(
        left,
        text=doctor["full_name"],
        bg="white",
        font=("Segoe UI", 14, "bold")
    ).pack(pady=(10, 2))

    tk.Label(
        left,
        text=doctor["full_name"],
        bg="white",
        fg="#777",
        font=("Segoe UI", 10)
    ).pack()

    tk.Label(
        left,
        text="Employee ID : DR-0001",
        bg="white",
        fg="#777",
        font=("Segoe UI", 9)
    ).pack(pady=(4, 10))

    tk.Button(
        left,
        text="Send Message",
        bg="#0d6efd",
        fg="white",
        font=("Segoe UI", 10),
        bd=0,
        padx=20,
        pady=6,
        cursor="hand2"
    ).pack()

    # ---------- RIGHT (INFO TABLE) ----------
    right = tk.Frame(top, bg="white")
    right.pack(side="right", fill="both", expand=True, padx=(80, 0))

    def info_row(parent, label, value):
        row = tk.Frame(parent, bg="white")
        row.pack(anchor="w", pady=6)

        tk.Label(row, text=label, width=12,
                 anchor="w", bg="white",
                 font=("Segoe UI", 10, "bold")).pack(side="left")

        tk.Label(row, text=value,
                 bg="white", fg="#0d6efd",
                 font=("Segoe UI", 10)).pack(side="left")

    info_row(right, "Phone:", doctor["phone"])
    info_row(right, "Email:", doctor["email"])
    info_row(right, "Birthday:", doctor["dob"])
    info_row(right, "Address:", doctor["address"])
    info_row(right, "Gender:", doctor["Gender"])
    #
    # # ===================== TABS =====================
    tabs = tk.Frame(content_frame, bg="white")
    tabs.pack(fill="x", padx=30)

    tk.Button(
        tabs, text="About", bd=0, bg="white",
        font=("Segoe UI", 10, "bold"), fg="#0d6efd"
    ).pack(side="left", padx=20, pady=10)

    tk.Button(
        tabs, text="Profile", bd=0, bg="white",
        font=("Segoe UI", 10)
    ).pack(side="left", padx=20)

    tk.Button(
        tabs, text="Messages", bd=0, bg="white",
        font=("Segoe UI", 10)
    ).pack(side="left", padx=20)

    # # ===================== EDUCATION =====================
    edu = tk.Frame(content_frame, bg="white", bd=1, relief="solid")
    edu.pack(fill="x", padx=30, pady=20)

    tk.Label(
        edu, text="Education Informations",
        bg="white",
        font=("Segoe UI", 12, "bold")
    ).pack(anchor="w", padx=20, pady=15)

    def edu_item(parent, title, degree, year):
        box = tk.Frame(parent, bg="white")
        box.pack(anchor="w", padx=40, pady=10)

        tk.Label(
            box, text=title,
            bg="white",
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w")

        tk.Label(
            box, text=degree,
            bg="white", fg="#777",
            font=("Segoe UI", 9)
        ).pack(anchor="w")

        tk.Label(
            box, text=year,
            bg="white", fg="#aaa",
            font=("Segoe UI", 8)
        ).pack(anchor="w")

    edu_item(
        edu,
        "International College of Medical Science (UG)",
        "MBBS",
        "2001 - 2003"
    )

    edu_item(
        edu,
        "International College of Medical Science (PG)",
        "MD - Obstetrics & Gynaecology",
        "1997 - 2001"
    )
