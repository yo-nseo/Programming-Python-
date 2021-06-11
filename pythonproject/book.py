#book.py

from contentsbook import contentsBook

class Book:
    def __init__(self):
        self.book_list = []

    def add_book(self): # 책 새로 추가
        # 책 추가
        new_book = contentsBook()
        new_book.set_book()
        self.book_list.append(new_book)

    def search_store(self):
        print('1. 관악')
        print('2. 영등포')
        print('3. 강남')
        store_search = input('원하는 서점을 선택하세요 : ')

    def show_book(self):
        for index, book in enumerate(self.book_list):
            print('-------------------')
            print(f'{index + 1}')
            print(book)
            print('-------------------\n')