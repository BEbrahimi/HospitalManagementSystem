import os
import tkinter as tk
from PIL import Image, ImageTk

def doctors_items(content_frame):


    # =========================
    # CARDS CONTAINER
    # =========================
    cards_frame = tk.Frame(content_frame, bg="#f5f7fa")
    cards_frame.pack(fill="both", expand=True, padx=20, pady=20)

    doctors = [
        ("Harshita", "Gynecologist", "Pune India", "doctor1.png"),
        ("Fatima Alizada", "Psychiatrist", "Pune India", "doctor2.png"),
        ("Harshita", "Gynecologist", "Pune India", "doctor1.png"),
        ("Fatima Alizada", "Psychiatrist", "Pune India", "doctor2.png"),
        ("Harshita", "Gynecologist", "Pune India", "doctor1.png"),
        ("Fatima Alizada", "Psychiatrist", "Pune India", "doctor2.png"),
        ("Fatima Alizada", "Psychiatrist", "Pune India", "doctor2.png"),
        ("Fatima Alizada", "Psychiatrist", "Pune India", "doctor2.png"),
        ("Harshita", "Gynecologist", "Pune India", "doctor1.png"),
        ("Fatima Alizada", "Psychiatrist", "Pune India", "doctor2.png"),
        ("Fatima Alizada", "Psychiatrist", "Pune India", "doctor2.png"),
        ("Fatima Alizada", "Psychiatrist", "Pune India", "doctor2.png"),
    ]

    card_width = 240
    card_height = 160
    gap_x = 50
    gap_y = 20
    cols = 4

    for index, (name, role, location, img_path) in enumerate(doctors):
        row = index // cols
        col = index % cols

        x = col * (card_width + gap_x)
        y = row * (card_height + gap_y)

        # ---------- Card ----------
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

        # ---------- Menu ----------
        tk.Label(
            card,
            text="⋮",
            bg="white",
            fg="#777",
            font=("Segoe UI", 14)
        ).place(x=210, y=10)

        # ---------- Avatar ----------
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        img_path = os.path.join(BASE_DIR, "..", "image", "doctor-03.jpg")
        img = Image.open(img_path).resize((60, 60))
        photo = ImageTk.PhotoImage(img)

        avatar = tk.Label(card, image=photo, bg="white")
        avatar.image = photo
        avatar.pack(pady=(15, 5))

        # ---------- Name ----------
        tk.Label(
            card,
            text=name,
            bg="white",
            fg="#000",
            font=("Segoe UI", 11, "bold")
        ).pack()

        # ---------- Role ----------
        tk.Label(
            card,
            text=role,
            bg="white",
            fg="#777",
            font=("Segoe UI", 9)
        ).pack()

        # ---------- Location ----------
        tk.Label(
            card,
            text=f"📍 {location}",
            bg="white",
            fg="#777",
            font=("Segoe UI", 9)
        ).pack(pady=(4, 0))


