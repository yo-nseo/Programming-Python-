#main.py

from book import Book

def print_menu():
    print("-------------------")
    print('\n1. 위치등록')
    print('2. 매장 검색')
    print('3. 책검색')
    print('4. 책등록')
    print('5. (서점 상관없이) 모든 책 보기')
    print('6. 종료하기\n')
    print("-------------------")
    num = input('메뉴를 선택하세요 : ')
    return num

def main():
    book = Book()
    while True:
        num = print_menu()
        if num == '1':
            # 사용자 위치 등록
            break
        elif num == '2':
            # 지역에 있는 매장 보여주기
            break
        elif num == '3':
            # 책 검색 후 그 책이 있는 매장 보여주기
            break
        elif num == '4':
            # 책 등록
            book.add_book()
        elif num == '5':
            # 서점 상관없이 책 목록 보여주기
            book.show_book()
        elif num == '6':
            break
        else:
            print('해당 메뉴가 없습니다.')

if __name__ == '__main__':
    main()