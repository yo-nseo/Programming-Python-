class Celebrity:
    def __init__(self, name):
        #pass #아무내용도 없을때
        self.name = name

    def set_name(self, name):
        self.name = name

    def set_entertainment(self, entertainment):
        self.entertainment = entertainment

    def info(self):
        print(f'이름 : {self.name}\t소속사 : {self.entertainment}')

    def __str__(self):
        return f'이름 : {self.name}\t소속사 : {self.entertainment}'

class Talent(Celebrity):
    def __init__(self, name):
        super().__init__(name)  #Celebrity 클래스(부모클래스)의 생성자 호출

    def set_drama(self, drama):
        self.drama = drama

    def __str__(self):
        #return f'이름 : {self.name}\t소속사 : {self.entertainment}\t드라마 : {self.drama}'
        return super().__str__() + f'\t드라마 : {self.drama}'

class Singer(Celebrity):
    def __init__(self, name, song):
        super().__init__(name)      #self.name = name
        self.song = song

    def __str__(self):
        return super().__str__() + f'\t노래 : {self.song}'

IU = Celebrity('이지은')
#IU.set_name('이지은')
IU.set_entertainment('이담')
# IU.info()
# print(IU.name, IU.entertainment)
print(IU)

이광수 = Talent('이광수')
이광수.set_entertainment('킹콩')
이광수.set_drama('라이브')
print(이광수)

현진 = Singer('현진', '신메뉴')
현진.set_entertainment('JYP')
print(현진)
필릭스 = Singer('필릭스', 'Back Door')
필릭스.set_entertainment('JYP')
print(필릭스)