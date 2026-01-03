import os
import shutil
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import bcrypt
from HMS.db.databaseConnection import get_connection

def add_doc(
    full_name_ent, roles_ent, username_ent, email_ent,
    password_ent, confirm_password_ent, dob_ent, gender_var,
    address_ent, country_var, city_ent, state_var, postal_ent,
    phone_ent, bio_txt, status_var, avatar_path_var
):
    full_name = full_name_ent.get()
    roles = roles_ent.get()
    username = username_ent.get()
    email = email_ent.get()
    password = password_ent.get()
    confirm_password = confirm_password_ent.get()
    dob = dob_ent.get()
    gender = gender_var.get()
    address = address_ent.get()
    country = country_var.get()
    city = city_ent.get()
    state = state_var.get()
    postal = postal_ent.get()
    phone = phone_ent.get()
    bio = bio_txt.get("1.0", "end-1c")
    status = status_var.get()
    avatar = avatar_path_var.get()


    if not username or not email or not password or not phone:
        messagebox.showerror("Error", "All fields are required")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
        return

    if len(password)<8:
        messagebox.showerror("Error", "Passwords is week")
        return

    try:
        con = get_connection()
        cur = con.cursor()

        #  hash password
        hashed_password = bcrypt.hashpw(
            password.encode('utf-8'),
            bcrypt.gensalt()
        )
        # ➕ insert Doctor
        add_doctor = """
                INSERT INTO doctors (full_name, roles, username, email, password, dob, Gender, address,counter, city, state,postal, phone, image, bio, status)
                VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s,%s, %s)
                """
        values = (full_name,roles,username,email,hashed_password,dob,gender,address,country,state, city,postal,phone,avatar,bio,status)
        cur.execute(add_doctor, values)
        con.commit()

        messagebox.showinfo("Success", "Registration Successful")

        cur.close()
        con.close()
    except Exception as e:
        messagebox.showerror("Database Error", str(e))


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

    #  padding
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    return scroll_frame

def add_doctor_form(content_frame):
    form_area = scrollable_frame(content_frame)

    container = tk.Frame(form_area, bg="white")
    container.pack(fill="both", expand=True, padx=20)

    container.grid_columnconfigure(0, weight=1, uniform="x")
    container.grid_columnconfigure(1, weight=1, uniform="x")
    container.grid_columnconfigure(2, weight=1, uniform="x")
    container.grid_columnconfigure(3, weight=1, uniform="x")


    # ================= Title =================
    tk.Label(
        container,
        text="Add Doctor",
        bg="white",
        fg="#333",
        font=("Segoe UI", 18, "bold")
    ).grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 20))
    # =========================
    # VARIABLES
    # =========================
    gender_var = tk.StringVar(value="Male")
    status_var = tk.StringVar(value="Active")
    country_var = tk.StringVar()
    state_var = tk.StringVar()
    avatar_path_var = tk.StringVar(value="No file chosen")
    selected_avatar_path = None

    # =========================
    # GRID CONFIG
    # =========================
    for i in range(4):
        container.columnconfigure(i, weight=1, uniform="x")

    # =========================
    # HELPERS
    # =========================
    def create_label(text, row, col, required=False):
        tk.Label(
            container,
            text=text + (" *" if required else ""),
            bg="white",
            fg="#444",
            font=("Segoe UI", 10)
        ).grid(row=row, column=col, sticky="w", pady=(8, 4), padx=10)

    def create_entry(row, col, colspan=1, show=None):
        ent = tk.Entry(
            container,
            font=("Segoe UI", 10),
            relief="solid",
            bd=1
        )
        if show:
            ent.config(show=show)

        ent.grid(
            row=row,
            column=col,
            columnspan=colspan,
            sticky="we",
            padx=10,
            ipady=6
        )
        return ent

    def shorten_filename(name, max_len=30):
        return name if len(name) <= max_len else name[:max_len - 3] + "..."

    # =========================
    # BASIC INFO
    # =========================
    create_label("Full Name", 1, 0, True)
    create_label("Roles", 1, 2)

    full_name_ent = create_entry(2, 0, 2)
    roles_ent = create_entry(2, 2, 2)

    create_label("Username", 3, 0, True)
    create_label("Email", 3, 2, True)

    username_ent = create_entry(4, 0, 2)
    email_ent = create_entry(4, 2, 2)

    create_label("Password", 5, 0)
    create_label("Confirm Password", 5, 2)

    password_ent = create_entry(6, 0, 2, show="*")
    confirm_password_ent = create_entry(6, 2, 2, show="*")

    # =========================
    # DATE & GENDER
    # =========================
    create_label("Date of Birth", 7, 0)
    create_label("Gender", 7, 2)

    dob_ent = create_entry(8, 0, 2)

    tk.Radiobutton(
        container, text="Male",
        variable=gender_var, value="Male",
        bg="white"
    ).grid(row=8, column=2, sticky="w", padx=10)

    tk.Radiobutton(
        container, text="Female",
        variable=gender_var, value="Female",
        bg="white"
    ).grid(row=8, column=3, sticky="w", padx=10)

    # =========================
    # ADDRESS
    # =========================
    create_label("Address", 9, 0)
    address_ent = create_entry(10, 0, 4)

    # =========================
    # LOCATION
    # =========================
    create_label("Country", 11, 0)
    create_label("City", 11, 1)
    create_label("State / Province", 11, 2)
    create_label("Postal Code", 11, 3)

    style = ttk.Style()
    style.configure("Custom.TCombobox", padding=6)

    country_cb = ttk.Combobox(
        container,
        textvariable=country_var,
        values=["USA", "India", "Afghanistan"],
        style="Custom.TCombobox"
    )
    country_cb.grid(row=12, column=0, sticky="we", padx=10, ipady=4)

    city_ent = create_entry(12, 1)

    state_cb = ttk.Combobox(
        container,
        textvariable=state_var,
        values=["California", "Delhi", "Kabul"],
        style="Custom.TCombobox"
    )
    state_cb.grid(row=12, column=2, sticky="we", padx=10, ipady=4)

    postal_ent = create_entry(12, 3)

    # =========================
    # PHONE & AVATAR
    # =========================
    create_label("Phone", 13, 0)
    phone_ent = create_entry(14, 0, 2)

    create_label("Avatar", 13, 2)

    avatar_lbl = tk.Label(
        container,
        textvariable=avatar_path_var,
        bg="#f0f0f0",
        anchor="w",
        padx=10,
        font=("Segoe UI", 9),
        width=32,
        relief="solid",
        bd=1
    )
    avatar_lbl.grid(row=14, column=2, sticky="we", padx=10)

    saved_avatar_path = None

    def choose_image():
        global selected_avatar_path, saved_avatar_path

        selected_avatar_path = filedialog.askopenfilename(
            title="Select Avatar Image",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
        )

        if not selected_avatar_path:
            return

        # =========================
        # IMAGE FOLDER
        # =========================
        images_dir = "image"
        os.makedirs(images_dir, exist_ok=True)

        # =========================
        # KEEP ORIGINAL FILE NAME
        # =========================
        image_name = os.path.basename(selected_avatar_path)
        saved_avatar_path = os.path.join(images_dir, image_name)

        # =========================
        # CHECK DUPLICATE FILE
        # =========================
        if os.path.exists(saved_avatar_path):
            messagebox.showwarning(
                "Duplicate Image",
                "Please select another image it is duplicate"
            )
            return

        # =========================
        # COPY IMAGE
        # =========================
        try:
            shutil.copy(selected_avatar_path, saved_avatar_path)
        except Exception as e:
            messagebox.showerror("Image Error", str(e))
            return

        # =========================
        # SHOW FILE NAME
        # =========================
        avatar_path_var.set(shorten_filename(image_name))

        print("Saved Image Path:", saved_avatar_path)
    tk.Button(
        container,
        text="Choose File",
        command=choose_image
    ).grid(row=14, column=3, sticky="w", padx=10)

    # =========================
    # BIOGRAPHY
    # =========================
    create_label("Short Biography", 15, 0)

    bio_txt = tk.Text(
        container,
        height=4,
        font=("Segoe UI", 10),
        relief="solid",
        bd=1
    )
    bio_txt.grid(row=16, column=0, columnspan=4, sticky="we", padx=10, pady=(0, 10))

    # =========================
    # STATUS
    # =========================
    create_label("Status", 17, 0)

    tk.Radiobutton(
        container, text="Active",
        variable=status_var, value="Active",
        bg="white"
    ).grid(row=18, column=0, sticky="w", padx=10)

    tk.Radiobutton(
        container, text="Inactive",
        variable=status_var, value="Inactive",
        bg="white"
    ).grid(row=18, column=1, sticky="w", padx=10)

    # =========================
    # SUBMIT
    # =========================
    tk.Button(
        container,
        text="CREATE DOCTOR",
        bg="#0d6efd",
        fg="white",
        font=("Segoe UI", 11, "bold"),
        relief="flat",
        padx=30,
        pady=10,
        cursor="hand2",
        command=lambda: add_doc(
            full_name_ent, roles_ent, username_ent, email_ent,
            password_ent, confirm_password_ent, dob_ent, gender_var,
            address_ent, country_var, city_ent, state_var, postal_ent,
            phone_ent, bio_txt, status_var, avatar_path_var
        )
    ).grid(row=19, column=0, columnspan=4, pady=30)
