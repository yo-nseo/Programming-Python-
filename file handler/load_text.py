print('전체 한꺼번에 읽기')
f = open('text.txt', 'r', encoding='utf-8')
data = f.read()
f.close()

print(data)


print('한줄 씩 읽기')
f = open('text.txt', 'r', encoding='utf-8')
while True:
    line = f.readline()   # line: 이유빈:초로색\n
    if line == '':  # 빈칸이라면 끝내라
        break
    print(line.rstrip())     # line.replace('\n', '')
f.close()

print('전체를 한꺼번에 읽고, 줄 별로 리스트')
f = open('text.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()
for line in lines:
    # 고에스터 : 검은색
    # line = '고에스더:검은색'
    data = line.split(':')
    print('이름 : ' + data[0].rstrip() + '\t좋아하는 색 : ' + data[1].rstrip())
    
# quiz
# 이름 : 이유빈[tab] 좋아하는 색 : 초록색
# 이름 : 김효진[tab] 좋아하는 색 : 하늘색