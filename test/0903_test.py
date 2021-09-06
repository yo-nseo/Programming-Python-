'''
# 1번
phone_price = 59827
price = phone_price - (phone_price % 100)

print(price)
'''

'''
# 2번
grade = 56
r_grade = grade - (grade % 10)

print(r_grade)
'''

'''
# 3번
import random
print(random.randrange(1, 46))
print(random.randrange(1, 46))
print(random.randrange(1, 46))
print(random.randrange(1, 46))
print(random.randrange(1, 46))
print(random.randrange(1, 46))
'''

# import random
#
# alist = []  # 뽑은 a를 넣어 중복 방지해주는 리스트
# for i in range(3):
#     a = random.randint(1, 9)
#     while a in alist:  # a가 이미 뽑은 리스트에 있을 때까지 다시 뽑자
#         a = random.randint(1, 9)
#     alist.append(a)  # 새로운 a 값을 리스트에 추가
# print(alist)

'''
import datetime
day1 = datetime.date(2021, 9, 3)
day2 = datetime.date(2022, 6, 18)
diff = day2 - day1
print(diff)
'''

# 8. 랜덤하게 번호로 자리를 배치하는 방법은? 제적(전출, 자퇴) 인원이 있다면?

import random

# 마지막 번호 묻자
last_number = input("마지막 번호는 ? : ")
# 1 ~ 마지막번호까지 숫자 리스트 만들자
list_class = list(range(1, int(last_number) + 1))
print(list_class)
# 빼자
while True:
# 반복
    # 뺄번호 묻자
    exclude_number = input("뺄 번호는 ? (enter치면 그만 빼기): ")
    # 다 뺐으면 반복 끝내자
    if exclude_number == '':
        break
    # 빼자
    list_class.remove(int(exclude_number))
    print(list_class)

# 섞자
random.shuffle(list_class)
# 출력하자
print('자리\t학생번호')
for i, number in enumerate(list_class):
    print(f'{i + 1}\t{number}')