# 1. x,y 좌표값을 가진 사각형 면적 구하기

# set함수는 중복된 값을 제거해준다.
result = set()
for i in range(4):  # 4번을 반복한다.
    x1, y1, x2, y2 = map(int,input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            # 사각형의 가로, 세로 길이 구할때 for문을 이렇게 이중으로 해서 가로, 세로 구해주기!
            result.add((x, y))
            # set 함수에 넣어줄때 add 하면 된다!
print(len(result))


# 두 번째 방법
field = [[False for i in range(100)] for j in range(100)]
# 사각형 전부를 False 값으로 채워준다.

for i in range(4):  # 4번 돈다
    x1, y1, x2, y2 = map(int,input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):  # for문 두번 돌려서 가로 세로길이 구한다.
            field[y][x] = True    # 사각형 면적만큼 True로 채워준다.
num = 0  # 값 넣어줄 빈 그릇
for row in range(100):
    num += field[row].count(True)
print(num)

