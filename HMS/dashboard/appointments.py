import tkinter as tk

# -------------------------------
# Upcoming Appointments Section
# -------------------------------
def create_upcoming_appointments(parent):

    parent.configure(bg="white")

    # -------- Header --------
    header = tk.Frame(parent, bg="white")
    header.pack(fill="x", padx=15, pady=(10, 5))

    tk.Label(
        header,
        text="Upcoming Appointments",
        bg="white",
        font=("Segoe UI", 12, "bold")
    ).pack(side="left")

    tk.Button(
        header,
        text="View all",
        bg="#0d6efd",
        fg="white",
        font=("Segoe UI", 9, "bold"),
        relief="flat",
        padx=14
    ).pack(side="right")

    # -------- Table Header --------
    table_head = tk.Frame(parent, bg="#f8f9fa")
    table_head.pack(fill="x", padx=15)

    headers = ["Patient", "Appointment With", "Timing", ""]
    for i, text in enumerate(headers):
        table_head.grid_columnconfigure(i, weight=1)

        tk.Label(
            table_head,
            text=text,
            bg="#f8f9fa",
            font=("Segoe UI", 9, "bold"),
            anchor="w"
        ).grid(row=0, column=i, padx=10, pady=9, sticky="ew")

    # -------- Table Body --------
    body = tk.Frame(parent, bg="white")
    body.pack(fill="both", expand=True, padx=15, pady=(0, 10))

    data = [
        ("Bernardo Galaviz", "New York, USA", "Dr. Cristina Groves", "7.00 PM"),
        ("Bernardo Galaviz", "New York, USA", "Dr. Cristina Groves", "7.00 PM"),
        ("Bernardo Galaviz", "New York, USA", "Dr. Cristina Groves", "7.00 PM"),
        ("Bernardo Galaviz", "New York, USA", "Dr. Cristina Groves", "7.00 PM"),
    ]

    for row in data:
        add_row(body, row)


def add_row(parent, row_data):

    row = tk.Frame(
        parent,
        bg="white",
        highlightthickness=1,
        highlightbackground="#eaeaea"
    )
    row.pack(fill="x", pady=4)

    for i in range(4):
        row.grid_columnconfigure(i, weight=1)

    # -------- Patient --------
    patient_frame = tk.Frame(row, bg="white")
    patient_frame.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    avatar = tk.Label(
        patient_frame,
        text=row_data[0][0],
        bg="#adb5bd",
        fg="white",
        width=2,
        font=("Segoe UI", 10, "bold")
    )
    avatar.pack(side="left", padx=(0, 8))

    info = tk.Frame(patient_frame, bg="white")
    info.pack(side="left")

    tk.Label(info, text=row_data[0], bg="white",
             font=("Segoe UI", 9, "bold")).pack(anchor="w")
    tk.Label(info, text=row_data[1], bg="white",
             fg="#6c757d", font=("Segoe UI", 8)).pack(anchor="w")

    # -------- Appointment With --------
    tk.Label(
        row,
        text=row_data[2],
        bg="white",
        font=("Segoe UI", 9)
    ).grid(row=0, column=1, sticky="w", padx=10)

    # -------- Timing --------
    tk.Label(
        row,
        text=row_data[3],
        bg="white",
        fg="#6c757d",
        font=("Segoe UI", 9)
    ).grid(row=0, column=2, sticky="w", padx=10)

    # -------- Button --------
    tk.Button(
        row,
        text="Take up",
        fg="#0d6efd",
        bg="white",
        relief="solid",
        borderwidth=1,
        font=("Segoe UI", 9),
        padx=16
    ).grid(row=0, column=3, sticky="e", padx=15)
