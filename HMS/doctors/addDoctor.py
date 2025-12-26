import tkinter as tk
from tkinter import ttk

def add_doctor_form(parent):

    container = tk.Frame(parent, bg="white")
    container.pack(fill="both", expand=True, padx=30, pady=20)

    # ================= Title =================
    tk.Label(
        container,
        text="Add Doctor",
        bg="white",
        fg="#333",
        font=("Segoe UI", 18, "bold")
    ).grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 20))

    # ================= Styles =================
    def label(text, r, c, req=False):
        tk.Label(
            container,
            text=text + (" *" if req else ""),
            bg="white",
            fg="#444",
            font=("Segoe UI", 10)
        ).grid(row=r, column=c, sticky="w", pady=(8, 4), padx=(0, 10))

    def entry(r, c, colspan=1, show=None):
        e = tk.Entry(
            container,
            font=("Segoe UI", 10),
            relief="solid",
            bd=1
        )
        if show:
            e.config(show=show)
        e.grid(row=r, column=c, columnspan=colspan,
               sticky="we", padx=(0, 20), ipady=6)
        return e

    # ================= Grid Config =================
    for i in range(4):
        container.columnconfigure(i, weight=1)

    # ================= Row 1 =================
    label("First Name", 1, 0, True)
    label("Last Name", 1, 2)

    entry(2, 0, colspan=2)
    entry(2, 2, colspan=2)

    # ================= Row 2 =================
    label("Username", 3, 0, True)
    label("Email", 3, 2, True)

    entry(4, 0, colspan=2)
    entry(4, 2, colspan=2)

    # ================= Row 3 =================
    label("Password", 5, 0)
    label("Confirm Password", 5, 2)

    entry(6, 0, colspan=2, show="*")
    entry(6, 2, colspan=2, show="*")

    # ================= Row 4 =================
    label("Date of Birth", 7, 0)
    label("Gender:", 7, 2)

    entry(8, 0, colspan=2)

    gender = tk.StringVar()
    tk.Radiobutton(container, text="Male", variable=gender, value="Male",
                   bg="white").grid(row=8, column=2, sticky="w")
    tk.Radiobutton(container, text="Female", variable=gender, value="Female",
                   bg="white").grid(row=8, column=3, sticky="w")

    # ================= Address =================
    label("Address", 9, 0)
    entry(10, 0, colspan=4)

    # ================= Location =================
    label("Country", 11, 0)
    label("City", 11, 1)
    label("State/Province", 11, 2)
    label("Postal Code", 11, 3)

    country = ttk.Combobox(container, values=["USA", "India", "Afghanistan"])
    country.grid(row=12, column=0, sticky="we", ipady=4, padx=(0, 10))

    entry(12, 1)
    state = ttk.Combobox(container, values=["California", "Delhi", "Kabul"])
    state.grid(row=12, column=2, sticky="we", ipady=4, padx=(0, 10))
    entry(12, 3)

    # ================= Submit Button =================
    tk.Button(
        container,
        text="Save Doctor",
        bg="#0d6efd",
        fg="white",
        font=("Segoe UI", 10, "bold"),
        relief="flat",
        padx=20,
        pady=8,
        cursor="hand2"
    ).grid(row=13, column=0, pady=25, sticky="w")
