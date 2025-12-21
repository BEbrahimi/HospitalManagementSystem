from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from db.databaseConnection import get_connection

# ----------------
# All Functions
# ----------------
def openLogin():
    root.destroy()
    import LoginFrom


# Functions
def register_user():
    username = userNameEnt.get()
    email = emailEnt.get()
    password = passwordEnt.get()
    re_password = re_passwordEnt.get()
    phone = phoneEnt.get()

    if not username or not email or not password or not phone:
        messagebox.showerror("Error", "All fields are required")
        return

    if password != re_password:
        messagebox.showerror("Error", "Passwords do not match")
        return

    if len(password)<8:
        messagebox.showerror("Error", "Passwords is week")
        return

    try:
        con = get_connection()
        cur = con.cursor()

        sql = """INSERT INTO hms_users (fullName, email, password, phone)
                 VALUES (%s, %s, %s, %s)"""
        values = (username, email, password, phone)

        cur.execute(sql, values)
        con.commit()

        messagebox.showinfo("Success", "Registration Successful")

        cur.close()
        con.close()

    except Exception as e:
        messagebox.showerror("Database Error", str(e))


# ----------------
# Main window
# ----------------

root = Tk()
root.title("Register")
root.configure(bg="#f2f2f2")
root.resizable(False,False)
width = 1100
height = 700
s_width = root.winfo_screenwidth()
s_height = root.winfo_screenheight()
center_x = int((s_width - width) / 2)
center_y = int((s_height - height) / 2)
root.geometry(f"{width}x{height}+{center_x}+{center_y}")
root.state("zoomed")

# ----------------
# center frame
# ----------------

card = Frame(root, bg="#fff",width=450,height=670)
card.place(relx=0.5,rely=0.5, anchor="center")
# ----------------
#  frame Shadow
# ----------------
shadow = Frame(root, bg="#d9d9d9",width=453,height=673)
shadow.place(relx=0.5,rely=0.5, anchor="center")
card.lift()

# ----------------
#  image
# ----------------

img = Image.open("image/logo-dark.png")
img = img.resize((80,80))

logo_img = ImageTk.PhotoImage(img)
logo_lbl = Label(card, image=logo_img,bg="#fff",width=80,height=80)
logo_lbl.image = logo_img
logo_lbl.place(x=185,y=20)

# ----------------
#  Entry and label
# ----------------

Label(card,text="User Name",
      bg="#fff",
      fg="#555",
      font=("Arial",12)).place(x=20,y=120)

userNameEnt = Entry(card,
    bg="#fff",
    bd=1,font=("Arial",12),relief = "solid" )
userNameEnt.place(x=22,y=160, width=400,height=35)



Label(card,text="Email Address",
      bg="#fff",
      fg="#555",
      font=("Arial",12)).place(x=20,y=210)

emailEnt = Entry(card,
    bg="#fff",
    bd=1,font=("Arial",12),relief = "solid" )
emailEnt.place(x=22,y=250, width=400,height=35)


Label(card,text="Password",
      bg="#fff",
      fg="#555",
      font=("Arial",12)).place(x=20,y=300)

passwordEnt = Entry(card,
    bg="#fff",
    bd=1,font=("Arial",12),relief = "solid",show="*" )
passwordEnt.place(x=22,y=340, width=400,height=35)


Label(card,text="RePassword",
      bg="#fff",
      fg="#555",
      font=("Arial",12)).place(x=20,y=390)

re_passwordEnt = Entry(card,
    bg="#fff",
    bd=1,font=("Arial",12),relief = "solid",show="*" )
re_passwordEnt.place(x=22,y=430, width=400,height=35)



Label(card,text="Mobile",
      bg="#fff",
      fg="#555",
      font=("Arial",12)).place(x=20,y=470)

phoneEnt = Entry(card,
    bg="#fff",
    bd=1,font=("Arial",12),relief = "solid" )
phoneEnt.place(x=22,y=510, width=400,height=35)


# ----------------
#  Button
# ----------------

signIn_btn = Button(card,text="SIGNUP",bg="#0A9CFF",
    fg="#fff",font=("Arial",12,"bold"),bd=0,height=2,command=register_user)
signIn_btn.place(x=180,y=570,width=80)

Label(card,text="I have already account",
      bg="#fff",
      fg="#555",
      font=("Arial",12)).place(x=120,y=630)
back_btn = Button(card,text="Click Here",bg="#fff",
    fg="#555",font=("Arial",9),bd=0,cursor="hand2",command=openLogin)
back_btn.place(x=275,y=630,width=80)

root.mainloop()