
class Icecream:
    def __init__(self, name): #생성자
        self.name = name

    def set_explanation(self, explanation):
        self.explanation = explanation

    def __str__(self): #객체를 우리가 알아보기 쉽게 문자열로 리턴. 주로 print()에서 호출
        return f'이름 : {self.name}'

'''
아이스홈런볼 = Icecream('아이스홈런볼')
아이스홈런볼.set_explanation('초콜릿 아이스크림, 바닐라 아이스크림')
print(아이스홈런볼)
print(아이스홈런볼.explanation)

오레오쿠키앤크림 = Icecream('오레오쿠키앤크림')
오레오쿠키앤크림.set_explanation('부드러운 바닐라향 아이스크림에, 달콤하고 진한 오레오 쿠키가 듬뿍!')
print(오레오쿠키앤크림)
print(오레오쿠키앤크림.explanation)

뉴욕치즈케이크 = Icecream('뉴욕치즈케이크')
뉴욕치즈케이크.set_explanation('부드럽게 즐기는 뉴욕식 정통 치즈케이크 아이스크림')
print(뉴욕치즈케이크)
print(뉴욕치즈케이크.explanation)

이상한나라의솜사탕 = Icecream('이상한나라의솜사탕')
이상한나라의솜사탕.set_explanation('부드럽고 달콤한 솜사탕과 함께 떠나는 이상한 나라로의 여행')
print(이상한나라의솜사탕)
print(이상한나라의솜사탕.explanation)
'''

class Order:
    _CATEGORIES = ('싱글레귤러', '더블레귤러', '파인트')
    _PRICES = (3200, 6200, 8200)

    def __init__(self):
        self.set_cateries() #종류
        self.menu = [] #메뉴
        self.init_menu()
        self.order_menu = [] #주문한 메뉴

    def __str__(self):
        pass

    def set_cateries(self):
        for index, category in enumerate(Order._CATEGORIES):
            print(index + 1, category)
        category_num = input('종류를 골라주세요: ')
        self.category = int(category_num)

    def init_menu(self):
        self.menu.append(Icecream('오레오쿠키앤크림'))
        self.menu.append(Icecream('뉴욕치즈케이크'))
        self.menu.append(Icecream('이상한나라의솜사탕'))

    def show_menu(self):
        for index, icecream in enumerate(self.menu):
            print(f'{index + 1}. {icecream}')

    def order(self):
        self.show_menu() #메뉴 보여주기
        for i in range(self.category): #종류에 따라 반복
            #   메뉴 선택
            icecream = input('아이스크림을 골라주세요 : ')
            icecream = int(icecream)

            #   주문한 메뉴에 추가
            self.order_menu.append(self.menu[icecream - 1])

        # 종류 출력
        print('-' * 10 + '주문 내역입니다' + '-' * 10)
        print(Order._CATEGORIES[self.category - 1])
        print(str(Order._PRICES[self.category - 1]) + '원')

        # 주문한 메뉴 출력
        for icecream in self.order_menu:
            print(icecream)

order = Order()
order.order()