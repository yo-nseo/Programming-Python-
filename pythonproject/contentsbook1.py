class contentsBook1:
    def __init__(self, title, writer, original_price, state):
        # 제목
        self.title = title
        # 글쓴이
        self.writer = writer
        # 정가
        self.original_price = original_price
        # 상태
        self.state = state
        # 가격
        self.price = self.setPrice()

    def setPrice(self):
        pass

