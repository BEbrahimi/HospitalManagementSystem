import tkinter as tk
from tkinter import messagebox, Image
from PIL import Image, ImageTk
from db.databaseConnection import get_connection
# -------------------------
# All Functions
# -------------------------
def goToReg():
    root.destroy()
    import registerFrom


def loginUser():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT * FROM hms_users 
        WHERE (email=%s OR fullname=%s) AND password=%s
        """
        cursor.execute(query, (username, username, password))
        result = cursor.fetchone()

        conn.close()

        if result:
            messagebox.showinfo("Success", "Login Successful")
            root.destroy()
            # import dashboard   # open next window
        else:
            messagebox.showerror("Error", "Invalid username or password")

    except Exception as e:
        messagebox.showerror("Database Error", str(e))


# -------------------------
# Main Window
# -------------------------
root = tk.Tk()
root.title("Login")
root.configure(bg="#f2f2f2")
root.resizable(False, False)
width = 1100
height = 700
s_width = root.winfo_screenwidth()
s_height = root.winfo_screenheight()
center_x = int((s_width - width) /2)
center_y = int((s_height - height) / 2)
root.geometry(f"{width}x{height}+{center_x}+{center_y}")
root.state("zoomed")

# -------------------------
# Center Frame (Card)
# -------------------------

card = tk.Frame(root, bg="white", width=450, height=440)
card.place(relx=0.5, rely=0.5, anchor="center")

# Shadow effect (optional)
shadow = tk.Frame(root, bg="#d9d9d9", width=453, height=443)
shadow.place(relx=0.5, rely=0.5, anchor="center")
card.lift()

img = Image.open("image/logo-dark.png")
img = img.resize((80, 80), Image.LANCZOS)  # width x height

logo_img = ImageTk.PhotoImage(img)
logo_label = tk.Label(card, image=logo_img, bg="white",width=80, bd=0)
logo_label.image = logo_img   # 🔴 VERY IMPORTANT
logo_label.place(x=185, y=20)




tk.Label(card, text="Username or Email",
         bg="white", fg="#555",
         font=("Arial", 12)).place(x=20, y=120)

username_entry = tk.Entry(card, font=("Arial", 12), bd=1, relief="solid")
username_entry.place(x=22, y=160,width=400,height=35)
# user_border = tk.Frame(card, bg="#0a9cff")  # border color
# user_border.place(x=22, y=190, width=400, height=2)

# # -------------------------
# # Password
# # -------------------------
tk.Label(card, text="Password",
         bg="white", fg="#555",
         font=("Arial", 12)).place(x=20, y=210)

password_entry = tk.Entry(card, font=("Arial", 12),
                          bd=1, relief="solid", show="*")
password_entry.place(x=22, y=250,width=400,height=35)

# -------------------------
# Forgot Password
# -------------------------
forgot = tk.Label(card, text="Forgot your password?",
                  bg="white", fg="#0a9cff",
                  font=("Arial", 9), cursor="hand2")
forgot.place(x=22, y=300)

# -------------------------
# Login Button
# -------------------------

login_btn = tk.Button(card, text="LOGIN",
                      bg="#0a9cff", fg="white",
                      font=("Arial", 12, "bold"),
                      bd=0, height=2,command=loginUser)
login_btn.place(x=180, y=350, width= 80)



# -------------------------
# Register Text
# -------------------------


tk.Label(card, text="Don't have an account?",
         bg="white", fg="#555",
         font=("Arial", 9)).place(x=120, y=410)

backBtn = tk.Button(card, text="Click here",
                      bg="white", fg="#555",
                      font=("Arial", 9),
                      bd=0,cursor="hand2",command=goToReg)
backBtn.place(x=250, y=410, width= 95)


# -------------------------
root.mainloop()
