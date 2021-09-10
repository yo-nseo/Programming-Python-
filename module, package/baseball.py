answer = make_answer()
print(answer)
# 무한 반복
while True:
    # 숫자 묻자
    guess = input("뭘까 ? : ")
    # strike, ball 판정하자
    strike, ball = check(guess, answer)
    print(f'{guess}\tstrike : {strike}, ball: {ball}')

    if answer == guess:
        print('정답입니다.')
        break