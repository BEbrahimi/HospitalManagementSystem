import tkinter as tk
from tkinter import ttk

import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

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

    # ⭐ بسیار مهم: بدون padding
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    return scroll_frame

def add_doctor_form(content_frame):
    form_area = scrollable_frame(content_frame)

    container = tk.Frame(form_area, bg="white")
    container.pack(fill="both", expand=True, padx=20, pady=20)
    # ================= Title =================
    tk.Label(
        container,
        text="Add Doctor",
        bg="white",
        fg="#333",
        font=("Segoe UI", 18, "bold")
    ).grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 20))

    # ================= Helpers =================
    def label(text, r, c, req=False):
        tk.Label(
            container,
            text=text + (" *" if req else ""),
            bg="white",
            fg="#444",
            font=("Segoe UI", 10)
        ).grid(row=r, column=c, sticky="w", pady=(8, 4))

    def entry(r, c, colspan=1, show=None):
        e = tk.Entry(container, font=("Segoe UI", 10), relief="solid", bd=1)
        if show:
            e.config(show=show)
        e.grid(row=r, column=c, columnspan=colspan,
               sticky="we", padx=(0, 20), ipady=6)
        return e

    for i in range(4):
        container.columnconfigure(i, weight=1)

    # ================= Basic Info =================
    label("First Name", 1, 0, True)
    label("Last Name", 1, 2)
    entry(2, 0, 2)
    entry(2, 2, 2)

    label("Username", 3, 0, True)
    label("Email", 3, 2, True)
    entry(4, 0, 2)
    entry(4, 2, 2)

    label("Password", 5, 0)
    label("Confirm Password", 5, 2)
    entry(6, 0, 2, show="*")
    entry(6, 2, 2, show="*")

    label("Date of Birth", 7, 0)
    label("Gender:", 7, 2)
    entry(8, 0, 2)

    gender = tk.StringVar(value="Male")
    tk.Radiobutton(container, text="Male", variable=gender,
                   value="Male", bg="white").grid(row=8, column=2, sticky="w")
    tk.Radiobutton(container, text="Female", variable=gender,
                   value="Female", bg="white").grid(row=8, column=3, sticky="w")

    # ================= Address =================
    label("Address", 9, 0)
    entry(10, 0, 4)

    # ================= Location =================
    label("Country", 11, 0)
    label("City", 11, 1)
    label("State/Province", 11, 2)
    label("Postal Code", 11, 3)

    ttk.Combobox(container, values=["USA", "India", "Afghanistan"]) \
        .grid(row=12, column=0, sticky="we", padx=(0, 10))
    entry(12, 1)
    ttk.Combobox(container, values=["California", "Delhi", "Kabul"]) \
        .grid(row=12, column=2, sticky="we", padx=(0, 10))
    entry(12, 3)

    # ================= Phone & Avatar =================
    label("Phone", 13, 0)
    entry(14, 0, 2)

    label("Avatar", 13, 2)

    avatar_img = tk.Label(container, bg="#eee", width=50, height=3)
    avatar_img.grid(row=14, column=2, sticky="w")

    def choose_image():
        file = filedialog.askopenfilename(
            filetypes=[("Images", "*.png *.jpg *.jpeg")]
        )
        if file:
            img = Image.open(file).resize((20, 20))
            photo = ImageTk.PhotoImage(img)
            avatar_img.config(image=photo)
            avatar_img.image = photo

    tk.Button(
        container,
        text="Choose file",
        command=choose_image
    ).grid(row=14, column=3, sticky="w")

    # ================= Biography =================
    label("Short Biography", 15, 0)
    bio = tk.Text(container, height=4, font=("Segoe UI", 10),
                  relief="solid", bd=1)
    bio.grid(row=16, column=0, columnspan=4,
             sticky="we", pady=(0, 10))

    # ================= Status =================
    label("Status", 17, 0)
    status = tk.StringVar(value="Active")

    tk.Radiobutton(container, text="Active", variable=status,
                   value="Active", bg="white").grid(row=18, column=0, sticky="w")
    tk.Radiobutton(container, text="Inactive", variable=status,
                   value="Inactive", bg="white").grid(row=18, column=1, sticky="w")

    # ================= Submit =================
    tk.Button(
        container,
        text="CREATE DOCTOR",
        bg="#0d6efd",
        fg="white",
        font=("Segoe UI", 11, "bold"),
        relief="flat",
        padx=30,
        pady=10,
        cursor="hand2"
    ).grid(row=19, column=0, columnspan=4, pady=30)
