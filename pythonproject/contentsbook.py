#contentsbook.py

class contentsBook:
    def __init__(self):
        # 글쓴이
        self.writer = ''
        # 제목
        self.title = ''
        # 연도
        self.year = ''
        # 정가
        self.original_price = ''
        # 상태
        self.state = ''
        # 가격
        self.price = ''
        # 서점
        self.bookstore = ''

    # 서점 설정
    def set_bookstore(self):
        print('1. 관악')
        print('2. 영등포')
        print('3. 강남')
        bookstore = input('어느 서점인가요? : ')
        self.bookstore = '입력된 정보가 없습니다. 처음으로 돌아갑니다' if bookstore == "" else bookstore


    def set_writer(self):
        writer = input('작가를 입력하세요 : ')
        self.writer = '미상' if writer == "" else writer

    def set_title(self):
        title = input('제목을 입력하세요 : ')
        self.title = '제목을 꼭 입력해주세요.' if title == "" else title

    def set_year(self):
        year = input('책 출시 연도를 적으세요 : ')
        self.year = '' if year == "" else year

    def set_original_price(self):
        original_price = input('원가를 입력하세요 : ')
        self.original_price = '' if original_price == "" else original_price

    def set_state(self):
        print("1. 매우 좋음")
        print("2. 좋음")
        print("3. 보통")
        print("4. 나쁨")
        state = input('상태를 입력하세요 : ')
        self.state = '' if state == "" else state

    def set_price(self):
        price = input('가격 입력하세요 : ')
        self.price = '' if price == "" else price

    def __str__(self):
        return f'서점 : {self.bookstore}\n작가 : {self.writer}\n제목 : {self.title}\n연도 : {self.year}\n정가 : {self.original_price}\n상태 : {self.state}\n가격 : {self.price}'


    def set_book(self):
        self.set_bookstore()
        self.set_writer()
        self.set_title()
        self.set_year()
        self.set_original_price()
        self.set_state()
        self.set_price()
