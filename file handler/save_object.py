from person import Person

# 객체 생성하자
num15 = Person('이재령', '하양색')
num17 = Person('임사랑', '분홍색')

# 리스트 만들자
bf = [num15, num17]

# 저장하자
# 1. 객체 하나 저장
import pickle

with open('object.bin', 'wb') as f:
    pickle.dump(num15, f)

# 2. 객체 여러 개 저장
with open('object.bin', 'wb') as f:
    pickle.dump(bf, f)