from baseball_game_engine import make_answer, check
from custom_error import InvalidLengthError

answer = make_answer()
# print(answer)
count = 0
# 무한 반복
while True:
    # 숫자 묻자
    guess = input("뭘까 ? : ")
    # 숫자인지 판정
    try:
        guess_int = int(guess)
    except ValueError as e:
        print('숫자를 입력하세요')
        continue

    if len(guess) != len(answer):
        # raise InvalidLengthError('정답의 길이와 같지 않습니다.')
        print(f'정답의 길이와 다른것을 입력했네요. {len(answer)} 문자')
        continue

    # strike, ball 판정하자
    strike, ball = check(guess, answer)
    count += 1
    # 출력하자
    print(f'{guess}\tstrike : {strike}, ball: {ball}\t{count}try')

    if answer == guess:
        print('정답입니다.')
        break