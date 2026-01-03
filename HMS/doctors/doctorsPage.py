import os
import tkinter as tk
from tkinter import messagebox

from PIL import Image, ImageTk
from HMS.db.databaseConnection import get_connection
from HMS.doctors.rount import show_doctor_details



def select_doctor():
    try:
        con = get_connection()
        cur = con.cursor()

        query = """
        SELECT id, full_name, roles, address, image
        FROM doctors
        ORDER BY id DESC
        """
        cur.execute(query)

        doctors = cur.fetchall()

        cur.close()
        con.close()

        return doctors

    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return []

def doctors_items(content_frame):

    # =========================
    # CONTAINER FOR ALL CARDS
    # =========================
    cards_frame = tk.Frame(content_frame, bg="#f5f7fa")
    cards_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # =========================
    # DOCTORS DATA
    # =========================
    doctors = select_doctor()

    # =========================
    # CARD LAYOUT SETTINGS
    # =========================
    card_width = 240
    card_height = 170
    gap_x = 40
    gap_y = 20
    cols = 4

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # =========================
    # CREATE CARDS
    # =========================
    for index, (doctor_id, name, role, location, img_name) in enumerate(doctors):
        row = index // cols
        col = index % cols

        x = col * (card_width + gap_x)
        y = row * (card_height + gap_y)

        # ---------- CARD ----------
        card = tk.Frame(
            cards_frame,
            bg="white",
            width=card_width,
            height=card_height,
            highlightthickness=1,
            highlightbackground="#e0e0e0"
        )
        card.place(x=x, y=y)
        card.pack_propagate(False)

        # ---------- MENU ICON ----------
        tk.Button(
            card,
            bd=0,
            text="⋮",
            bg="white",
            fg="#777",
            font=("Segoe UI", 14),

        ).place(x=210, y=8)

        # ---------- AVATAR ----------
        image_path = os.path.join(BASE_DIR, "..", "image", img_name)


        if not os.path.exists(image_path):
            image_path = os.path.join(BASE_DIR, "..", "image", "user.jpg")

        img = Image.open(image_path).resize((60, 60))
        photo = ImageTk.PhotoImage(img)

        avatar = tk.Button(card, image=photo, bg="white",cursor= "hand2",bd=0,
                           command=lambda d_id=doctor_id: show_doctor_details(content_frame, d_id)
)
        avatar.image = photo
        avatar.pack(pady=(18, 6))

        # ---------- NAME ----------
        tk.Label(
            card,
            text=name,
            bg="white",
            fg="#000",
            font=("Segoe UI", 11, "bold")
        ).pack()

        # ---------- ROLE ----------
        tk.Label(
            card,
            text=role,
            bg="white",
            fg="#777",
            font=("Segoe UI", 9)
        ).pack()

        # ---------- LOCATION ----------
        tk.Label(
            card,
            text=f"📍 {location}",
            bg="white",
            fg="#777",
            font=("Segoe UI", 9)
        ).pack(pady=(4, 0))