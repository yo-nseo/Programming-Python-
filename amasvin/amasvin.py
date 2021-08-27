class Drink:
    _CUPS = ('레귤러', '점보')                   #레귤러
    _ICES = ('0%', '50%', '100%', '150%')      #100%
    _SUGARS = ('0%', '50%', '100%', '150%')    #100%
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cup = 0    #'레귤러'
        self.ice = 2    #'100%'
        self.suger = 2  #'100%'

    def set_cup(self):
        for index, cup in enumerate(Drink._CUPS): #컵 종류 보여주기
            print(f'{index + 1}: {cup}')

        cup = input('컵 사이즈를 선택하세요 : ') #컵 선택
        if cup == '':
            self.cup = 0
        else:
            cup = int(cup)
            self.cup = cup - 1 #컵 self에 넣기

        if self.cup == 1: #점보일때 +500원
            self.price += 500

    def set_ice(self):
        for index, ice in enumerate(Drink._ICES): #얼음량 종루 보여주기
            print(f'{index + 1}: {ice}')
        ice = input('얼음량을 선택하세요: ') #선택하기
        # if ice == '':
        #     self.ice = 2
        # else:
        #     self.ice = int(ice) - 1
        self.ice = 2 if ice == '' else int(ice) - 1 #self.ice에 설정하기

    def set_sugar(self):
        for index, sugar in enumerate(Drink._SUGARS): #당도 보여주기
            print(f'{index + 1}: {sugar}')
        sugar = input('당도를 선택하세요: ') #당도 선택하기
        self.suger = 2 if sugar == '' else int(sugar) - 1 #self.sugar에 넣기

    def order(self):
        self.set_cup()
        self.set_ice()
        self.set_sugar()

    def __str__(self):
        return f'이름: {self.name}\t가격: {self.price}\t컵사이즈: {Drink._CUPS[self.cup]}\t얼음량: {Drink._ICES[self.ice]}\t당도: {Drink._SUGARS[self.suger]}'

class Coffee(Drink):
    pass

class Bubbletea(Drink):
    _PEARLS = ('타피오카', '화이트', '알로에', '젤리')

    def __init__(self, name, price):
        super().__init__(name, price) #부모초기화 호출
        self.pearl = 0 # 타피오카

    def set_pearl(self):
        for index, pearl in enumerate(Bubbletea._PEARLS): # 펄 종류 보여주기
            print(f'{index + 1}: {pearl}')
        pearl = input('펄 종류를 선택하세요 : ') # 펄 선택하기
        self.pearl = 0 if pearl == '' else int(pearl) - 1 # self.pearl에 넣기

    def order(self):
        super().order() # 부모 클래스의 order() 호출하기
        self.set_pearl() # set_pearl() 호출하기
        pass

    def __str__(self):
        result = super().__str__()
        return result + f'\t펄 종류 : {Bubbletea._PEARLS[self.pearl]}'
        # 부모클래스의 __str__()(이름, 가격, 컵사이즈, 얼음량, 당도, 펄)
        pass


class Order:
    def __init__(self):
        self.menu = [] # self.menu 매장에 있는 음료수 전체
        self.init_menu() # init_menu()
        self.order_menu = [] # self.order_menu 내가 고른 메뉴들

    def init_menu(self):
        사랑이꺼 = Coffee('카페모카', 2500)
        하람이꺼 = Bubbletea('오레오 쉐이크', 3900)
        에스더꺼 = Bubbletea('타로 밀크티', 3300)
        self.menu.append(사랑이꺼)
        self.menu.append(하람이꺼)
        self.menu.append(에스더꺼)

    def show_menu(self):
        for index, drink in enumerate(self.menu):
            print(f'{index + 1}: {drink.name} {drink.price}원')

    def sum_price(self):
        sum_value = 0 # self.order_menu 하나씩 꺼내서 그 Drink의 가격을 합계내고 리턴
        for drink in self.order_menu:
            sum_value += drink.price
        return sum_value

    def order_drink(self):
        while True: #반복
            self.show_menu() # 메뉴 보여주기
            drink = input('메뉴를 선택하세요 : ') # 메뉴 선택하기
            drink = int(drink) - 1
            new_drink = self.menu[drink]
            new_drink.order() # 옵션 선택하기
            self.order_menu.append(new_drink) # self.order_menu에 추가하기
            is_add = input('더 주문하기겠습니까? (n : 종료)') # 더 주문 하기
            if is_add == 'n':
                break
        print(self) #주문 내역 보여주기
    
    def __str__(self):
        s = '-' * 20 + '주문 내역' + '-' * 20 + '\n' # 주문 내역 제목 보여주기
        for drink in self.order_menu: # 주문한 음료수들 목록 보여주기
            s += str(drink) + '\n'
        s += f'총 금액: {self.sum_price()}원' # 총 합계 가격 보여주기
        return s

# 사랑이꺼 = Drink('밀크티', 2500)
# 사랑이꺼.order()
# print(사랑이꺼)
# 하람이꺼 = Bubbletea('오레오 쉐이크', 3900)
# 하람이꺼.o
# print(하람이꺼)
order = Order()
order.order_drink()