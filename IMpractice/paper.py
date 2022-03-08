# 색종이의 면적을 겹치지 않고 구하는 문제

n = int(input)
total = []
for i in range(n):   # n개의 색종이
    a,b,c,d = map(int,input().split())
    square= set()
    for i in range(a, a+c):
        for j in range(b, b+d):
            square.add((i, j))


# 여기서부터 코드 리뷰 분석 - 희원님 #

import sys
N = int(input())
# 1000*1000 필드에 모조리 0으로 채워준다
field = [[0 for i in range(1001)] for j in range(1001)]

for i in range(1, N + 1): # n번을 반복
    # x1, y1은 사각형이 시작하는 지점
    # width, length는 실제 사각형의 세로 가로 길이이다.
    x1, y1, width, length = map(int,sys.stdin.readline().strip().split())
    # 여기서 sys.stdin.readline().strip()은 input()과 똑같은 역할을 한다.
    # 다만 input()보다 더 빠르게 수를 받을 수 있어서 사용!! 
    # 위의 import sys와 함께 사용해준다.
    x2 = x1 + width    # x2, y2는 시작하는 지점에서 실제 사각형 길이를 더한 끝나는 지점
    y2 = y1 + length
    for y in range(y1, y2):  # 사각형이 시작하는 지점에서 끝나는 지점까지 순환
        # 한꺼번에 대입하는게 시간단축에 중요한 역할을 함
        field[y][x1:x2] = [i] * width

    count = [0 for i in range(N)]
    for line in field:   # 0으로 채워진 field안을 순회
        for i in range(1, N + 1):   # 색종이 갯수만큼 번복
            count[i-1] += line.count(i) 

    for i in range(N):
        print(count[i])


# 석현님 코드 #
N = int(input())

recs = []
for num in range(N):   # N번만큼 순회. 색종이 장수만큼임
    r, c, w, h = map(int,input().split())   # 마찬가지로 시작점들과 사각형 세로가로길이
    points = set([])   # 이전 rectangle 문제처럼 빈 set 그릇을 준비한다.
    for x in range(r, r+ w):
        for y in range(c, c + h):  # 마찬가지로 가로 세로 길이를 구해준다.
            points.add((x,y))   # x, y 는 찐 가로세로 길이임
            # 여기서 range(len(points)) 하면 면적이 된다.
        for i in range(len(recs)):   
            recs[i] -= points   
        recs.append(points)
    for i in range(N):
        print(len(recs[i]))  # 색종이 면적 출력


#  동현님 코드
# 1번 면적에는 전부 1 부여
# 2번 면적에는 전부 2 부여...
# 각각의 번호를 센다

n = int(input())
area = [[0] * 1001 for i in range(1001)]     # 빈 리스트에 0으로 채워넣기

for i in range(1, n+1):
    x, y, w, h = map(int, input().split())   # 좌표값 받기
    for y in range(y, y+h):                  # y의 범위
        area[y][x:x+w] = [i] * w             # 해당 범위에 숫자 넣기 / 이중 for문으로 돌리지 않고, 행 단위로 돌게 만들어 시간 단축
                                   
for i in range(1, n+1):                      # 1~n+1 번호 순회
    tot_cnt = 0                              # 초기화
    for m in area:                           # area 순회
        tot_cnt += m.count(i)                # 숫자 세기
    print(tot_cnt)

# 이중 for문 대신 행 단위로 for문을 한번만 돌게하여 시간단축
# 숫자를 세는 마지막 문단도 count함수를 써서 단순화시킴


#  근혜님 코드
# 색종이 장수
N = int(input())
# [가장 왼쪽 아래 좌표, 너비, 높이]
paper_lst = [list(map(int, input().split())) for i in range(N)]
# print(b)
# ex)
# 2
# 0 0 2 2
# 1 1 3 3
# => [[0,0,2,2],[1,1,3,3]]

plane = [[0]*1001 for _ in range(1001)]   # 1000개로 채워진 0 필드

for i in range(N):  # n 번을 반복
    for j in range(paper_lst[i][0], paper_lst[i][0] + paper_lst[i][2]):  # 
        for k in range(paper_lst[i][1], paper_lst[i][1] + paper_lst[i][3]):
            plane[j][k] = i + 1  # 해당 색종이 영역
# print(plane)

# 해당 색종이 칸수 세기
for i in range(N):
    cnt = 0
    for j in plane:
        cnt += j.count(i + 1)
    print(cnt)