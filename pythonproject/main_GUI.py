from tkinter import *
from tkinter.filedialog import *
from contentsbook import *

class main_gui():
    def __init__(self):
        self.init_gui()
        self.c_book = contentsBook()

    def init_gui(self):
        self.book_main = Tk()

        self.book_main.title("중고 서점")
        self.book_main.geometry("640x400+450+200")
        self.book_main.resizable(False, False)

        grid_x = 0
        grid_y = 0

        addBook_btn = Button(self.book_main, text="책 등록", relief=GROOVE, font=("Sunflower", "15"), command=self.add_book)
        addBook_btn.place(x=540, y=30)

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


    def file_button(self):
        self.filename = askopenfilename(initialdir='./png', title='파일선택', filetypes=(
            ('png files', '*.png'), ('jpg files', '*.jpg'), ('all files', '*.*')))


    def add_book(self):
        self.addBook = Toplevel(self.book_main)
        self.addBook.title("책 추가")
        self.addBook.geometry("400x400+550+200")
        self.addBook.resizable(False, False)

        w_title, w_writer, w_original = StringVar(), StringVar(), StringVar()
        self.Radio_chose = IntVar()

        s_good = Radiobutton(self.addBook, text="매우 좋음", value=1, variable=self.Radio_chose, command=self.check_state)
        s_nomal = Radiobutton(self.addBook, text="보통", value=2, variable=self.Radio_chose, command=self.check_state)
        s_bad = Radiobutton(self.addBook, text="나쁨", value=3, variable=self.Radio_chose, command=self.check_state)
        s_good.place(x=270, y=130)
        s_nomal.place(x=270, y=150)
        s_bad.place(x=270, y=170)

        b_title = Label(self.addBook, text="제목", font=("Sunflower", "13"))
        b_title.place(x=110, y=30)
        ent_title = Entry(self.addBook, textvariable=w_title)
        ent_title.place(x=155, y=31)

        b_writer = Label(self.addBook, text="작가", font=("Sunflower", "13"))
        b_writer.place(x=110, y=60)
        ent_writer = Entry(self.addBook, textvariable=w_writer)
        ent_writer.place(x=155, y=61)

        w_original = Label(self.addBook, text="정상가", font=("Sunflower", "13"))
        w_original.place(x=98, y=90)
        ent_original = Entry(self.addBook, textvariable=w_original)
        ent_original.place(x=155, y=91)

        fopen_btn = Button(self.addBook, text="이미지 업로드", relief=GROOVE, font=("Sunflower", "11"), command=self.file_button)
        fopen_btn.place(x=98, y=120)
        fname_lab = Label(self.addBook, text=self.filename)
        fname_lab.place(x=100, y=150)

        self.addBook.mainloop()




    def check_state(self):
        if str(self.Radio_chose.get()) == '1':
            print("매우 좋음")
        elif str(self.Radio_chose.get()) == '2':
            print("보통")
        else:
            print("나쁨")

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
