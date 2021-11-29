from tkinter import *

class main_gui():
    def __init__(self):
        self.init_gui()

    def init_gui(self):
        self.book_main = Tk()

        self.book_main.title("중고 서점")
        self.book_main.geometry("640x400+450+200")
        self.book_main.resizable(False, False)

        # book1
        book1_img = PhotoImage(file='hgp.gif')
        book1_imglbl = Label(self.book_main, image=book1_img)
        book1_imglbl.place(x=20, y=30)

        book1_button1 = Button(self.book_main, text="상세 정보", relief=GROOVE, font=("Sunflower", "11"), command=self.createNewWindow)
        book1_button1.place(x=130, y=40)
        book1_button2 = Button(self.book_main, text="장바구니에\n담기", relief=GROOVE, font=("Sunflower", "10"))
        book1_button2.place(x=130, y=80)
        book1_button3 = Button(self.book_main, text="구매하기", relief=GROOVE, font=("Sunflower", "11"))
        book1_button3.place(x=130, y=130)

        book1_label1 = Label(self.book_main, text="혼자 공부하는 파이썬", font=("Sunflower", "10"))
        book1_label1.place(x=20, y=160)
        book1_label2 = Label(self.book_main, text="18000원", font=("Sunflower", "10"), fg='#ff0000')
        book1_label2.place(x=20, y=177)

        self.book_main.mainloop()

    def createNewWindow(self):
        details = Toplevel(self.book_main)
        details.title("상세 정보")
        details.geometry("400x400+550+200")
        details.resizable(False, False)

        img_1 = PhotoImage(file="hgp1.gif")
        book1_dimg = Label(details, image=img_1)
        book1_dimg.place(x=20, y=30)

        details.mainloop()


if __name__ == '__main__':
    gui = main_gui()
