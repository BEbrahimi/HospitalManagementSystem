import tkinter as tk

from HMS.doctors.profile import doctors_profile


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
def open_doctor_details(content_frame, doctor_id):
    clear_frame(content_frame)

    # =========================
    # TOP BAR (Title + Button)
    # =========================
    top_bar = tk.Frame(content_frame, bg="#f5f7fa", height=60)
    top_bar.pack(fill="x", padx=20, pady=(10, 0))

    tk.Label(
        top_bar,
        text="My profile",
        bg="#f5f7fa",
        fg="#999",
        font=("Segoe UI", 18, "bold")
    ).pack(side="left")

    add_btn = tk.Button(
        top_bar,
        text="+Edit Profile",
        bg="#0d6efd",
        fg="white",
        font=("Segoe UI", 10, "bold"),
        relief="flat",
        padx=16,
        pady=6,
        cursor="hand2",
    )
    add_btn.pack(side="right")
    doctors_profile(doctor_id,content_frame)