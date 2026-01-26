import os
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from HMS.db.databaseConnection import get_connection

def create_scrollable_page(parent):
    canvas = tk.Canvas(parent, bg="#f5f5f5", highlightthickness=0)
    scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)

    scrollable_frame = tk.Frame(canvas, bg="#f5f5f5")

    window_id = canvas.create_window(
        (0, 0),
        window=scrollable_frame,
        anchor="nw"
    )

    def resize_frame(event):
        canvas.itemconfig(window_id, width=event.width)

    canvas.bind("<Configure>", resize_frame)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Mouse scroll
    canvas.bind_all(
        "<MouseWheel>",
        lambda e: canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")
    )

    return scrollable_frame






def invoice_list(content_frame):
    # =========================
    # Clear previous widgets
    # =========================
    for widget in content_frame.winfo_children():
        widget.destroy()
    scrollable_frame = create_scrollable_page(content_frame)

    # =========================
    # Title
    # =========================
    title = tk.Label(
        scrollable_frame,
        text="Invoice",
        font=("Segoe UI", 18, "bold"),

    )
    title.pack(anchor="w", padx=20, pady=(10, 15))

    # =========================
    # box Frame
    # =========================
    box_frame = tk.Frame(scrollable_frame, bg="white", width=100, height=470)
    box_frame.pack(fill="both", padx=30)
    left_frame = tk.Frame(box_frame, bg="#fff", width=400, height=470)
    left_frame.pack(side="left", fill="y", padx=2)
    right_frame = tk.Frame(box_frame, bg="#fff", width=400, height=470)
    right_frame.pack(side="right", fill="y", padx=2)



    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(BASE_DIR, "..", "image", "logo-dark.png")


    img = Image.open(img_path)
    img.thumbnail((90, 90), Image.LANCZOS)
    hospital_logo = ImageTk.PhotoImage(img)

    logo_lbl = tk.Label(
        left_frame,
        image=hospital_logo,
        bg="white"
    )
    logo_lbl.image = hospital_logo
    logo_lbl.place(x=30, y=30)

    tk.Label(
        left_frame,
        text="Ramoz Hospital",
        bg="#fff", fg="#888",
        font=("Segoe UI", 11, "bold"),
    ).place(x=20, y=150)

    tk.Label(
        left_frame,
        text="3864 Quiet Valley Lane,\nSherman Oaks, CA, 91403\nGST No:",
        bg="#fff", fg="#888",
        font=("Segoe UI", 11),
        justify="left",
        anchor="w"
    ).place(x=20, y=175)

    tk.Label(
        left_frame,
        text="Invoice to:",
        bg="#fff", fg="#888",
        font=("Segoe UI", 11),
    ).place(x=20, y=270)

    tk.Label(
        left_frame,
        text="Barry Cuda",
        bg="#fff", fg="#888",
        font=("Segoe UI", 11, "bold"),
    ).place(x=20, y=300)

    tk.Label(
        left_frame,
        text="Global Technologies \n5754 Airport Rd \nCoosada, AL, 36020 \nUnited States \n888-777-6655 \nbarrycuda@example.com",
        bg="#fff", fg="#888",
        justify="left",
        anchor="w",
        font=("Segoe UI", 11),
    ).place(x=20, y=330)

    tk.Label(
        right_frame,
        text="INVOICE #INV-0001",
        bg="#fff", fg="#888",
        justify="right",
        anchor="w",
        font=("Segoe UI", 20,"bold"),
    ).place(x=130, y=20)

    tk.Label(
        right_frame,
        text="Date: October 12, 2017 \nDue date: November 25, 2017",
        bg="#fff", fg="#888",
        justify="right",
        anchor="w",
        font=("Segoe UI", 13),
    ).place(x=140, y=60)

    inside_frame = tk.Frame(right_frame, bg="#fff", width=400, height=200)
    inside_frame.place(x=0,y=260)

    # Normal text (before)
    tk.Label(
        inside_frame,
        text="Payment Details:",
        bg="#fff",
        fg="#888",
        font=("Segoe UI", 11),
        anchor="w"
    ).place(x=0, y=30)

    # Bold line
    tk.Label(
        inside_frame,
        text="Total Due:",
        bg="#fff",
        fg="#888",
        font=("Segoe UI", 11, "bold"),
        anchor="w"
    ).place(x=0, y=55)

    # Rest normal
    tk.Label(
        inside_frame,
        text="Bank name:\nCountry:\nCity:\nAddress:\nIBAN\nSWIFT Code:",
        bg="#fff",
        fg="#888",
        justify="left",
        anchor="w",
        font=("Segoe UI", 11),
    ).place(x=0, y=80)


    # Bold line
    tk.Label(
        inside_frame,
        text="$ 288.2",
        bg="#fff",
        fg="#888",
        font=("Segoe UI", 11, "bold"),
        anchor="w"
    ).place(x=340, y=55)

    # Rest normal
    tk.Label(
        inside_frame,
        text="Azizi Bank\nAfghanistan\nKabul\nDashti Barch\nKFH56464654\nAPT4E",
        bg="#fff",
        fg="#888",
        justify="right",
        anchor="w",
        font=("Segoe UI", 11),
    ).place(x=300, y=80)

    style = ttk.Style()
    style.theme_use("clam")

    style.layout(
        "Invoice.Treeview",
        [('Treeview.treearea', {'sticky': 'nswe'})]
    )

    style.configure(
        "Invoice.Treeview",
        background="white",
        fieldbackground="white",
        borderwidth=0,
        relief="flat",
        rowheight=40
    )

    style.configure(
        "Invoice.Treeview.Heading",
        background="white",
        borderwidth=0,
        relief="flat",
        font=("Segoe UI", 12, "bold")
    )

    table_frame = tk.Frame(
        scrollable_frame,
        bg="white",
        bd=0,
        highlightthickness=0
    )
    table_frame.pack(fill="both", expand=True, padx=30, pady=2)
    columns = (
        "#", "ITEM", "DESCRIPTION","UNIT COST", "QUANTITY", "TOTAL"
    )

    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings",
        height=3,
        style="Invoice.Treeview"
    )

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")


    tree.column("#", width=10)
    tree.column("ITEM", width=120)
    tree.column("DESCRIPTION", width=260)
    tree.column("UNIT COST", width=120)
    tree.column("QUANTITY", width=100)
    tree.column("TOTAL", width=80)


    tree.pack(fill="both", expand=True)

    cost = 150
    qty = 2
    total = cost * qty
    # =========================
    # Insert Sample Data
    # =========================

    tree.insert("", "end",
                values=(1, "Full body", "Lorem ipsum dolor sit amet, consectetur adipiscing elit", f"$ {cost}", f"{qty}", f"${total}"),

    )
    tree.insert("", "end",
                values=(2, "Blood Test", "Lorem ipsum dolor sit amet, consectetur adipiscing elit", f"$ {cost}",
                        f"{qty}", f"${total}"),

                )
    tree.insert("", "end",
                values=(3, "General checkup", "Lorem ipsum dolor sit amet, consectetur adipiscing elit", f"$ {cost}",
                        f"{qty}", f"${total}"),

                )

    right_table = tk.Frame(scrollable_frame, bg="#fff", width=400, height=150)
    right_table.pack(anchor="e", pady=(0, 30),padx=(0, 30))

    tk.Label(
        right_table,
        text="Total due",
        bg="#fff",
        fg="#888",
        justify="left",
        anchor="w",
        font=("Segoe UI", 9),
    ).place(x=30, y=10)

    tk.Label(
        right_table,
        text="Subtotal:\n\nTax(10%):\n\nTotal:",
        bg="#fff",
        fg="#888",
        justify="left",
        anchor="w",
        font=("Segoe UI", 11,"bold"),
    ).place(x=30, y=40)

    tax = 0.10
    taxper = tax * 100

    final_total = total + taxper
    tk.Label(
        right_table,
        text=f"{total}$\n\n{taxper}%\n\n{final_total}$",
        bg="#fff",
        fg="#888",
        justify="left",
        anchor="w",
        font=("Segoe UI", 11, "bold"),
    ).place(x=330, y=40)

    description_frame = tk.Frame(scrollable_frame, bg="#fff", width=1600, height=150)
    description_frame.pack( anchor="w", pady=(0, 5),padx=(0, 30))

    tk.Label(
        description_frame,
        text="Other information\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus sed dictum ligula, cursus blandit risus. Maecenas eget metus non tellus\n dignissim aliquam ut a ex. Maecenas sed vehicula dui, ac suscipit lacus. Sed finibus leo vitae lorem interdum, eu scelerisque tellus fermentum.\n Curabitur sit amet lacinia lorem. Nullam finibus pellentesque libero, eu finibus sapien interdum vel",
        bg="#fff",
        fg="#888",
        justify="left",
        anchor="w",
        font=("Segoe UI", 11, "bold"),
    ).place(x=30, y=20)






