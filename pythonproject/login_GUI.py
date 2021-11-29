from tkinter import *
#import main_GUI

oldBook_login = Tk()

oldBook_login.title("중고 책 서점")
oldBook_login.geometry("640x400+450+200")
oldBook_login.resizable(False, False)

titleText = Label(oldBook_login, text="중고 책 서점", height=3, font=("Sunflower", "30"))
titleText.pack()

user_id, user_pw = StringVar(), StringVar()

def check_data():
    if user_id.get() == "admin" and user_pw.get() == "1234":
        print("Login Successfully")
        oldBook_login.destroy()
        #main_GUI.main_gui()
    else:
        print("Check your id / password")

text_id = Label(oldBook_login, text="ID", font=("Sunflower", "12"))
text_id.pack()
ent_id = Entry(oldBook_login, textvariable=user_id)
ent_id.pack()

text_pw = Label(oldBook_login, text="PW", font=("Sunflower", "12"))
text_pw.pack(pady=(5, 0))
ent_pw = Entry(oldBook_login, textvariable=user_pw)
ent_pw.config(show="*")
ent_pw.pack()

log_bnt = Button(oldBook_login, text="로그인", font="Sunflower", command=check_data, relief=GROOVE)
log_bnt.pack(pady=(10, 0))

oldBook_login.mainloop()