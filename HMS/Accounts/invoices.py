import tkinter as tk
from tkinter import ttk

def add_invoice_form(content_frame):

    # =========================
    # Clear previous widgets
    # =========================
    for widget in content_frame.winfo_children():
        widget.destroy()

    # =========================
    # Title
    # =========================
    title = tk.Label(
        content_frame,
        text="Invoices",
        font=("Segoe UI", 18, "bold"),

    )
    title.pack(anchor="w", padx=20, pady=(10, 15))

    # =========================
    # Filter Frame
    # =========================
    filter_frame = tk.Frame(content_frame, bg="white",width=100)
    filter_frame.pack(fill="x", padx=20)


    status_cb = ttk.Combobox(
        filter_frame,
        values=["Select Status", "Paid", "Sent", "Partially Paid"],
        state="readonly"
    )
    status_cb.current(0)

    search_btn = tk.Button(
        filter_frame,
        text="SEARCH",
        bg="#5AD164",
        fg="white",
        font=("Segoe UI", 10, "bold"),
        relief="flat",
        padx=30,
        pady=6
    )


    status_cb.grid(row=0, column=0,columnspan=3, padx=15)
    search_btn.grid(row=0, column=4, padx=10)

    # =========================
    # Table Frame
    # =========================
    table_frame = tk.Frame(content_frame, bg="white")
    table_frame.pack(fill="both", expand=True, padx=20, pady=15)

    columns = (
        "#", "Invoice Number", "Patient",
        "Created Date", "Due Date", "Amount", "Status","Action"
    )

    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings",
        height=10
    )

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    tree.column("#", width=40)
    tree.column("Invoice Number", width=120)
    tree.column("Patient", width=160)
    tree.column("Created Date", width=120)
    tree.column("Due Date", width=120)
    tree.column("Amount", width=80)
    tree.column("Status", width=120)
    tree.column("Action", width=120)

    tree.pack(fill="both", expand=True)

    # =========================
    # Tags for Status Colors
    # =========================
    tree.tag_configure("paid", background="#E8FFF1")
    tree.tag_configure("sent", background="#E8F3FF")
    tree.tag_configure("partial", background="#FFF3E0")

    # =========================
    # Insert Sample Data
    # =========================
    tree.insert("", "end",
                values=(1, "#INV-0001", "Charles Ortega", "1 Aug 2018", "7 Aug 2018", "$20", "Paid", "⋮"),
                tags=("paid",)
                )

    tree.insert("", "end",
                values=(2, "#INV-0002", "Denise Stevens", "24 Aug 2018", "24 Aug 2018", "$6", "Sent", "⋮"),
                tags=("sent",)
                )

    tree.insert("", "end",
                values=(3, "#INV-0003", "Dennis Salazar", "1 Sep 2018", "7 Sep 2018", "$20", "Partially Paid", "⋮"),
                tags=("partial",)
                )

    # =========================
    # Right Click Menu
    # =========================
    action_menu = tk.Menu(content_frame, tearoff=0)

    action_menu.add_command(label="✏️  Edit")
    action_menu.add_command(label="👁️  View")
    action_menu.add_command(label="⬇️  Download")
    action_menu.add_separator()
    action_menu.add_command(label="🗑️  Delete")

    def on_tree_click(event):
        region = tree.identify("region", event.x, event.y)
        if region != "cell":
            return

        column = tree.identify_column(event.x)
        row = tree.identify_row(event.y)
        if column == f"#{len(columns)}" and row:
            action_menu.tk_popup(event.x_root, event.y_root)

    tree.bind("<Button-1>", on_tree_click)
