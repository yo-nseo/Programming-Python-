from tkinter import *

oldBook = Tk()

oldBook.title("중고 책 서점")
oldBook.geometry("640x400+450+200")
oldBook.resizable(False, False)

titleText = Label(oldBook, text="중고 책 서점")

titleText.pack()

oldBook.mainloop()