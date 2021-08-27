class Recipe:
    def __init__(self, name):
        # 재료, 재료 양
        self.ingredient = {} # 빈 딕셔너리 생성
        # 내용
        self.contents = ''
        # 이름
        self.name = name
        # 몇 인분
        self.people = 1 # 기본값 1인분
        # 영상 링크
        self.video = ''


    def set_contents(self):
        contents = input('레시피 내용을 입력하세요 : ')
        self.contents = '입력된 정보가 없습니다.' if contents == "" else contents

    def set_people(self):
        people = input('몇 인분 인가요? : ')
        self.people = '1' if people == '' else people

    def set_video(self):
        video = input('레시피 영상 주소를 입력하세요 : ')
        self.video = '입력된 정보가 없습니다.' if video == "" else video

    def set_ingredient(self):
        while True:
            ingredient = input('재료를 입력하세요 : (ex - 감자 100)\n재료 입력이 끝났으면 엔터를 누르세요 : ')
            if ingredient == '':
                break

            ingredient_name, ingredient_gram = ingredient.split()
            self.ingredient[ingredient_name] = ingredient_gram
            # {'감자' : '200', '당근' : '100'}


    def __str__(self):
        return f'레시피 : {self.name}\n양 : {self.people}인분\n정보 : {self.contents}\n영상 링크 : {self.video}\n재료 : {self.ingredient}'

    def set_recipe(self):
        self.set_people()
        self.set_ingredient()
        self.set_contents()
        self.set_video()
    
# 카레 = Recipe('카레')
# 카레.set_recipe()
# print(카레)