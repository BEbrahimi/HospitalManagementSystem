from PIL import Image, ImageTk
import tkinter as tk

from common.dashboard import dashboard_items
# =======================
# Root Window
# =======================
root = tk.Tk()
root.title("Hospital Management Dashboard")
root.geometry("1300x750")
root.config(bg="#f5f7fa")
root.resizable(False,False)
root.state("zoomed")

# =======================
# HEADER
# =======================
header = tk.Frame(root, bg="#0d6efd", height=60)
header.pack(fill="x")

# Load & Resize Image
logo_img = Image.open("image/logo.png")
logo_img = logo_img.resize((32, 32), Image.LANCZOS)
logo_icon = ImageTk.PhotoImage(logo_img)
# Label with Image + Text
logo_label = tk.Label(
    header,
    image=logo_icon,
    text=" Hospital",
    compound="left",
    bg="#0d6efd",
    fg="white",
    font=("Segoe UI", 16, "bold")
)
logo_label.image = logo_icon  # جلوگیری از Garbage Collection
logo_label.pack(side="left", padx=20, pady=15)

# ---------- Admin Icon ----------
admin_btn = tk.Menubutton(
    header,
    text=" Admin ⬇",
    bg="#0a71ae",
    activebackground="#0a71ae",
    relief="flat",
    fg="#fff",
    cursor="hand2",
    font=("Segoe UI",10,"bold")
)
admin_menu = tk.Menu(admin_btn, tearoff=0)
admin_menu.add_command(label="Profile")
admin_menu.add_command(label="Edit Profile")
admin_menu.add_separator()
admin_menu.add_command(label="Logout")

admin_btn.config(menu=admin_menu)
admin_btn.pack(side="right", padx=20)


# =======================
# MAIN BODY
# =======================
main = tk.Frame(root, bg="#f5f7fa")
main.pack(fill="both", expand=True)

# =======================
# SIDEBAR
# =======================
sidebar = tk.Frame(main, bg="#0d6efd", width=220)
sidebar.pack(side="left", fill="y")

# tk.Label(
#     sidebar, text="Main",
#     bg="white",
#     font=("Segoe UI", 11, "bold")
# ).pack(anchor="w", padx=20, pady=10)

# =======================
# CONTENT AREA
# =======================
content_frame = tk.Frame(main, bg="#f5f7fa")
content_frame.pack(side="right", fill="both", expand=True)

# =======================
# Helper Function
# =======================
def clear_content():
    for widget in content_frame.winfo_children():
        widget.destroy()

# =======================
# Pages
# =======================
def show_dashboard():
    clear_content()
    dashboard_items(content_frame)

def show_doctors():
    clear_content()
    tk.Label(
        content_frame,
        text="👨‍⚕️ Doctors Page",
        font=("Segoe UI", 20, "bold"),
        bg="#f5f7fa"
    ).pack(pady=40)

def show_patients():
    clear_content()
    tk.Label(
        content_frame,
        text="🧑 Patients Page",
        font=("Segoe UI", 20, "bold"),
        bg="#f5f7fa"
    ).pack(pady=40)

def show_appointments():
    clear_content()
    tk.Label(
        content_frame,
        text="📅 Appointments Page",
        font=("Segoe UI", 20, "bold"),
        bg="#f5f7fa"
    ).pack(pady=40)

def show_invoices():
    clear_content()
    tk.Label(
        content_frame,
        text="🧾 Invoices Page",
        font=("Segoe UI", 20, "bold"),
        bg="#f5f7fa"
    ).pack(pady=40)

def show_payments():
    clear_content()
    tk.Label(
        content_frame,
        text="💳 Payments Page",
        font=("Segoe UI", 20, "bold"),
        bg="#f5f7fa"
    ).pack(pady=40)

# =======================
# Accounts Dropdown Logic
# =======================
accounts_open = False

def toggle_accounts():
    global accounts_open
    if accounts_open:
        accounts_submenu.pack_forget()
        accounts_btn.config(text="Accounts ⌄")
    else:
        accounts_submenu.pack(fill="x")
        accounts_btn.config(text="Accounts ⌃")
    accounts_open = not accounts_open

# =======================
# Sidebar Buttons
# =======================

dLogo = ImageTk.PhotoImage(file="icon/dashboard.png")
doctor = ImageTk.PhotoImage(file="icon/doctor.png")
patient = ImageTk.PhotoImage(file="icon/patient.png")

tk.Button(
    sidebar,
    image=dLogo,
    text="Dashboard",
    compound="left",
    bg="#0d6efd", fg="#fff",
    font=("Segoe UI", 11),
    relief="flat", anchor="w",
    padx=6,
    command=show_dashboard
).pack(fill="x", pady=4)


tk.Button(
    sidebar, image= doctor,
    compound="left",
    text="Doctors",
    bg="#0d6efd", fg="#fff",
    font=("Segoe UI", 11),
    relief="flat", anchor="w",
    padx=6,
    command=show_doctors
).pack(fill="x", pady=4)

tk.Button(
    sidebar,
    image= patient,
    compound="left",
    text="Patients",
    bg="#0d6efd", fg="#fff",
    font=("Segoe UI", 11),
    relief="flat", anchor="w",
    padx=6,
    command=show_patients
).pack(fill="x", pady=4)

tk.Button(
    sidebar, text="Appointments",
    bg="#0d6efd", fg="#fff",
    font=("Segoe UI", 11),
    relief="flat", anchor="w",
    padx=20,
    command=show_appointments
).pack(fill="x", pady=4)

# ---------- Accounts Dropdown ----------
accounts_btn = tk.Button(
    sidebar,
    text="Accounts ⌄",
    bg="#0d6efd", fg="#fff",
    font=("Segoe UI", 11),
    relief="flat",
    anchor="w",
    padx=20,
    command=toggle_accounts
)
accounts_btn.pack(fill="x", pady=4)

accounts_submenu = tk.Frame(sidebar, bg="#f2f2f2")

tk.Button(
    accounts_submenu,
    text="Invoices",
    bg="#0d6efd", fg="#fff",
    font=("Segoe UI", 10),
    relief="flat",
    anchor="w",
    padx=30,
    command=show_invoices
).pack(fill="x", pady=2)

tk.Button(
    accounts_submenu,
    text="Payments",
    bg="#f2f2f2",
    fg="#555",
    font=("Segoe UI", 10),
    relief="flat",
    anchor="w",
    padx=30,
    command=show_payments
).pack(fill="x", pady=2)

# =======================
# Default Page
# =======================
show_dashboard()

root.mainloop()
