import tkinter as tk

def create_doctors_section(parent):

    parent.configure(bg="white")

    # ---------- Title ----------
    title = tk.Label(
        parent,
        text="Doctors",
        bg="white",
        font=("Segoe UI", 12, "bold")
    )
    title.pack(anchor="w", padx=15, pady=(10, 5))

    # ---------- Canvas + Scrollbar ----------
    canvas = tk.Canvas(
        parent,
        bg="white",
        highlightthickness=0
    )
    canvas.pack(side="left", fill="both", expand=True, padx=(10, 0))

    scrollbar = tk.Scrollbar(
        parent,
        orient="vertical",
        command=canvas.yview
    )
    scrollbar.pack(side="right", fill="y", padx=(0, 5))

    canvas.configure(yscrollcommand=scrollbar.set)

    # ---------- Scrollable Frame ----------
    scrollable_frame = tk.Frame(canvas, bg="white")
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Update scroll region
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # ---------- Doctors Data ----------
    doctors = [
        ("Bashir Ebrahimi", "MBBS, MD"),
        ("Bashir Ebrahimi", "MBBS, MD"),
        ("Bashir Ebrahimi", "MBBS, MD"),
        ("Bashir Ebrahimi", "MBBS, MD"),
        ("Bashir Ebrahimi", "MBBS, MD"),
        ("Bashir Ebrahimi", "MBBS, MD"),

    ]

    for name, degree in doctors:
        add_doctor_row(scrollable_frame, name, degree)

    # ---------- Footer ----------
    footer = tk.Label(
        parent,
        text="View all Doctors",
        bg="white",
        fg="#6c757d",
        font=("Segoe UI", 9)
    )
    footer.pack(pady=5)


def add_doctor_row(parent, name, degree):

    row = tk.Frame(parent, bg="white")
    row.pack(fill="x", padx=10, pady=6)

    # Avatar
    avatar = tk.Label(
        row,
        text="B",
        bg="#adb5bd",
        fg="white",
        width=2,
        font=("Segoe UI", 10, "bold")
    )
    avatar.pack(side="left", padx=(0, 10))

    # Info
    info = tk.Frame(row, bg="white")
    info.pack(side="left", fill="x", expand=True)

    tk.Label(
        info,
        text=name,
        bg="white",
        font=("Segoe UI", 9, "bold")
    ).pack(anchor="w")

    tk.Label(
        info,
        text=degree,
        bg="white",
        fg="#6c757d",
        font=("Segoe UI", 8)
    ).pack(anchor="w")


