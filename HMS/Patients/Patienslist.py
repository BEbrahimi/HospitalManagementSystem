import os
import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image


def patient_list(content_frame):

    # =========================
    # SAMPLE DATA
    # =========================
    data = [
        ("Roshan", 35, "Pune university 411020", "724654554", "roshan@example.com")
    ] * 13

    # =========================
    # VARIABLES
    # =========================
    entries_var = tk.IntVar(value=10)
    current_page = tk.IntVar(value=1)

    # =========================
    # STYLE
    # =========================
    style = ttk.Style()
    style.theme_use("default")

    style.configure(
        "Treeview",
        background="#ffffff",
        foreground="#333333",
        rowheight=46,
        fieldbackground="#ffffff",
        font=("Segoe UI", 10)
    )

    style.configure(
        "Treeview.Heading",
        font=("Segoe UI", 11, "bold"),
        background="#f1f3f6",
        foreground="#000000"
    )

    style.map(
        "Treeview",
        background=[("selected", "#e3f2fd")]
    )

    # =========================
    # TOP BAR
    # =========================
    top_frame = tk.Frame(content_frame, bg="#ffffff")
    top_frame.pack(fill="x", padx=20, pady=12)

    tk.Label(
        top_frame,
        text="Show",
        bg="#ffffff",
        font=("Segoe UI", 11)
    ).pack(side="left")

    entries_box = ttk.Combobox(
        top_frame,
        textvariable=entries_var,
        values=[10, 20, 50],
        width=7,
        font=("Segoe UI", 11),
        state="readonly"
    )
    entries_box.pack(side="left", padx=8)

    tk.Label(
        top_frame,
        text="entries",
        bg="#ffffff",
        font=("Segoe UI", 11)
    ).pack(side="left")

    # =========================
    # TABLE FRAME
    # =========================
    table_frame = tk.Frame(content_frame, bg="#ffffff")
    table_frame.pack(fill="both", expand=True, padx=20)

    columns = ("Name", "Age", "Address", "Phone", "Email", "Action")

    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="tree headings",
        height=10
    )

    # Column widths
    tree.column("#0", width=60, anchor="center")   # Avatar
    tree.heading("#0",)

    tree.column("Name", width=160)
    tree.column("Age", width=70, anchor="center")
    tree.column("Address", width=240,anchor="center")
    tree.column("Phone", width=140,anchor="center")
    tree.column("Email", width=220,anchor="center")
    tree.column("Action", width=200, anchor="center")

    for col in columns:
        tree.heading(col, text=col)

    tree.pack(side="left", fill="both", expand=True)

    # =========================
    # SCROLLBAR
    # =========================
    scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=tree.yview
    )
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # =========================
    # AVATAR IMAGE
    # =========================
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    IMAGE_PATH = os.path.join(BASE_DIR, "..", "image", "user.jpg")

    avatar_img = Image.open(IMAGE_PATH).resize((32, 32))
    avatar = ImageTk.PhotoImage(avatar_img)
    avatars = []
    # =========================
    # LOAD DATA
    # =========================
    def load_data():
        tree.delete(*tree.get_children())

        per_page = entries_var.get()
        page = current_page.get()

        start = (page - 1) * per_page
        end = start + per_page

        for row in data[start:end]:
            item = tree.insert(
                "",
                "end",
                image=avatar,
                values=(row[0], row[1], row[2], row[3], row[4], "⋮")
            )
            avatars.append(avatar)

        page_label.config(
            text=f"Showing {start+1} to {min(end, len(data))} of {len(data)} entries"
        )

    # =========================
    # PAGINATION
    # =========================
    pagination_frame = tk.Frame(content_frame, bg="#ffffff")
    pagination_frame.pack(fill="x", padx=20, pady=12)

    page_label = tk.Label(
        pagination_frame,
        text="",
        bg="#ffffff",
        font=("Segoe UI", 10)
    )
    page_label.pack(side="left")

    def prev_page():
        if current_page.get() > 1:
            current_page.set(current_page.get() - 1)
            load_data()

    def next_page():
        per_page = entries_var.get()
        max_page = (len(data) + per_page - 1) // per_page
        if current_page.get() < max_page:
            current_page.set(current_page.get() + 1)
            load_data()

    tk.Button(
        pagination_frame,
        text="Previous",
        width=11,
        command=prev_page
    ).pack(side="right", padx=6)

    tk.Button(
        pagination_frame,
        text="Next",
        width=11,
        command=next_page
    ).pack(side="right")

    # =========================
    # EVENTS
    # =========================
    entries_box.bind("<<ComboboxSelected>>", lambda e: load_data())

    # =========================
    # INITIAL LOAD
    # =========================
    load_data()

