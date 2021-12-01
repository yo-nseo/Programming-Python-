
from tkinter.filedialog import *
import tkinter.messagebox
from contentsbook1 import *

class main_gui():
    def __init__(self):
        self.init_gui()
        self.newBook = []


    def init_gui(self):
        self.book_main = Tk()

        self.book_main.title("중고 서점")
        self.book_main.geometry("640x400+450+200")
        self.book_main.resizable(False, False)

        addBook_btn = Button(self.book_main, text="책 등록", relief=GROOVE, font=("Sunflower", "15"), command=self.add_book)
        addBook_btn.place(x=540, y=30)

        # book1
        # book1_img = PhotoImage(file='hgp.gif')
        # book1_imglbl = Label(self.book_main, image=book1_img)
        # book1_imglbl.place(x=20, y=30)

        # book1_button1 = Button(self.book_main, text="상세 정보", relief=GROOVE, font=("Sunflower", "11"), command=self.createNewWindow)
        # book1_button1.place(x=130, y=40)
        book1_button2 = Button(self.book_main, text="구매하기", relief=GROOVE, font=("Sunflower", "10"), command=self.buy_book)
        book1_button2.place(x=130, y=80)
        # book1_button3 = Button(self.book_main, text="구매하기", relief=GROOVE, font=("Sunflower", "11"))
        # book1_button3.place(x=130, y=130)

        book1_label1 = Label(self.book_main, text="혼자 공부하는 파이썬", font=("Sunflower", "15"))
        book1_label1.place(x=50, y=40)
        book1_label2 = Label(self.book_main, text="18000원", font=("Sunflower", "12"), fg='#ff0000')
        book1_label2.place(x=50, y=80)

        self.book_main.mainloop()

    def add_book(self):
        self.addBook = Toplevel(self.book_main)
        self.addBook.title("책 추가")
        self.addBook.geometry("400x400+550+200")
        self.addBook.resizable(False, False)

        self.w_title, self.w_writer, self.w_original = StringVar(), StringVar(), StringVar()
        self.Radio_chose = IntVar()

        s_good = Radiobutton(self.addBook, text="매우 좋음", value=1, variable=self.Radio_chose, command=self.check_state)
        s_nomal = Radiobutton(self.addBook, text="보통", value=2, variable=self.Radio_chose, command=self.check_state)
        s_bad = Radiobutton(self.addBook, text="나쁨", value=3, variable=self.Radio_chose, command=self.check_state)
        s_good.place(x=170, y=130)
        s_nomal.place(x=170, y=150)
        s_bad.place(x=170, y=170)

        b_title = Label(self.addBook, text="제목", font=("Sunflower", "13"))
        b_title.place(x=110, y=30)
        ent_title = Entry(self.addBook, textvariable=self.w_title)
        ent_title.place(x=155, y=31)

        b_writer = Label(self.addBook, text="작가", font=("Sunflower", "13"))
        b_writer.place(x=110, y=60)
        ent_writer = Entry(self.addBook, textvariable=self.w_writer)
        ent_writer.place(x=155, y=61)

        b_original = Label(self.addBook, text="정상가", font=("Sunflower", "13"))
        b_original.place(x=98, y=90)
        ent_original = Entry(self.addBook, textvariable=self.w_original)
        ent_original.place(x=155, y=91)

        up_button = Button(self.addBook, text="등록하기", relief=GROOVE, command=self.new_book)
        up_button.place(x=170, y=200)


        # fopen_btn = Button(self.addBook, text="이미지 업로드", relief=GROOVE, font=("Sunflower", "11"), command=self.file_button)
        # fopen_btn.place(x=98, y=120)

        self.addBook.mainloop()

    def new_book(self):
        n_book = contentsBook1(self.w_title.get(), self.w_writer.get(), self.w_original.get(), self.Radio_chose.get())
        self.newBook.append(n_book)
        for book in self.newBook:
            print(f'{book.title}, {book.writer}, {book.original_price}, {book.state}')

    def buy_book(self):
        self.buyBook = Toplevel(self.book_main)
        self.buyBook.title("책 구매")
        self.buyBook.geometry("400x400+550+200")
        self.buyBook.resizable(False, False)

        buy_ch = Label(self.buyBook, text="책을 구매하시겠습니까?", font=("", "15")).pack(pady=(100, 0))
        buy_ok = Button(self.buyBook, text="구매", command=self.btn_ok).pack()
        buy_no = Button(self.buyBook, text="취소", command=self.btn_no).pack()

    def btn_ok(self):
        tkinter.messagebox.showinfo("구매 확인", "구매해주셔서 감사합니다!")
        self.buyBook.destroy()

        print('구매하기')

    def btn_no(self):
        self.buyBook.destroy()

    # def file_button(self):
    #     filename = askopenfilename(initialdir='./png', title='파일선택', filetypes=(
    #         ('png files', '*.png'), ('jpg files', '*.jpg'), ('all files', '*.*')))
    #     file_img = PhotoImage(file=filename)
    #     file_imglbl = Label(self.addBook, image=file_img)
    #     file_imglbl.place(x=100, y=200)


    def check_state(self):
        if str(self.Radio_chose.get()) == '1':
            print("매우 좋음")
        elif str(self.Radio_chose.get()) == '2':
            print("보통")
        else:
            print("나쁨")

    # def createNewWindow(self):
    #     details = Toplevel(self.book_main)
    #     details.title("상세 정보")
    #     details.geometry("400x400+550+200")
    #     details.resizable(False, False)
    #
    #     img_1 = PhotoImage(file="hgp1.gif")
    #     book1_dimg = Label(details, image=img_1)
    #     book1_dimg.place(x=20, y=30)
    #
    #     details.mainloop()


if __name__ == '__main__':
    gui = main_gui()
