from tkinter import *

oldBook_login = Tk()

oldBook_login.title("중고 책 서점")
oldBook_login.geometry("640x400+450+200")
oldBook_login.resizable(False, False)

titleText = Label(oldBook_login, text="중고 책 서점", width=10, height=5, font=("Sunflower", "30"))
titleText.pack()

user_id, user_pw = StringVar(), StringVar()

def check_data():
    if user_id.get() == "admin" and user_pw.get() == "1234":
        print("Loggin Successfully")
    else:
        print("Check your id / password")

text_id = Label(oldBook_login, text="ID")
text_id.pack()
ent_id = Entry(oldBook_login, textvariable=user_id)
ent_id.pack()

text_pw = Label(oldBook_login, text="PW")
text_pw.pack()
ent_pw = Entry(oldBook_login, textvariable=user_pw)
ent_pw.config(show="*")
ent_pw.pack()

log_bnt = Button(oldBook_login, text="로그인", font="Sunflower", command=check_data)
log_bnt.pack()

oldBook_login.mainloop()