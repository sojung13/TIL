import sys
sys.stdin = open('input.txt','r')

me = [list(map(int,input().split())) for _ in range(5)]
mc = [list(map(int,input().split())) for _ in range(5)]

#사회자 1차원 배열 >
mc_list = []
for x in range(5):
    for y in range(5):
        mc_list.append(mc[x][y])
# print(mc_list)  # [5, 10, 7, 16, 2, 4, 22, 8, 17, 13, 3, 18, 1, 6, 25, 12, 19, 23, 14, 21, 11, 24, 9, 20, 15]
bingo = [[0] * 5 for _ in range(5)]  # 임의의 가상 0 빙고판 만들기
for i in range(len(mc_list)):
    for r in range(5):
        for c in range(5):
            if mc_list[i] == me[r][c]:   # 사회자 리스트와 내 빙고판 맞는지 돌려주기
                bingo[r][c] = 1
                break
    cnt = 0
    # 가로로 빙고열 맞는지 확인하기
    for x in range(5):
        sum1 = 0
        for y in range(5):
            sum1 += bingo[x][y]
        if sum1 == 5:
            cnt += 1
    # 세로로 빙고열 맞는지 확인하기
    for y in range(5):
        sum2 = 0
        for x in range(5):
            sum2 += bingo[x][y]
        if sum2 == 5:
            cnt += 1
    # 대각선으로 빙고열 맞는지 확인하기
    sum3 = 0
    for x in range(5):
        sum3 += bingo[x][x]
    if sum3 == 5:
        cnt += 1
    # 반대 대각선으로 빙고열 맞는지 확인하기
    sum4 = 0
    for x in range(5):
        sum4 += bingo[x][4-x]
    if sum4 == 5:
        cnt += 1

    # 만약 빙고가 3줄 이상이면(줄별로 누적합 5가 되는 줄이 3개가 된다면)
    if cnt >= 3:
        print(i+1)
        break   # (4,5,6.... 이상의 줄은 필요없으므로 반복 종료!)


print(bingo)
# 만약 빙고판에 True가 맞게 잘 들어갔을 경우
# 순회하여 True가 같은 인덱스 행/열로 입력되었을 경우 + 1 (빙고줄 표시)
# 3이 되면 빙고 완성 > 모든 True의 갯수 반환

# arr = [list(map(int, input().split()))for _ in range(5)]
#
# MC = [list(map(int, input().split()))for _ in range(5)]
#
# call_mc = []
# # mc가 부르는 수 1차원리스트로 만들기
# for x in range(5):
#     for y in range(5):
#         call_mc.append(MC[x][y])
#
# # 부른거 정리할 배열
# called = [[0]*5 for _ in range(5)]
#
# for i in range(len(call_mc)):
#     for x in range(5):
#         for y in range(5):
#             # 사회자가 부른 숫자 위치에 체크
#             if call_mc[i] == arr[x][y]:
#                 called[x][y] = 1
#                 break
#     # 빙고체크 시작
#     # 가로 체크
#     cnt = 0
#     for x in range(5):
#         if sum(called[x]) == 5:
#             cnt += 1
#     # 대각선체크
#     s1 = 0
#     for x in range(5):
#         s1 += called[x][x]
#     if s1 == 5:
#         cnt += 1
#     # 반대 대각선 체크
#     s2 = 0
#     for x in range(5):
#         s2 += called[x][4-x]
#     if s2 == 5:
#         cnt += 1
#     # 세로 체크
#     for y in range(5):
#         s3 = 0
#         for x in range(5):
#             s3 += called[x][y]
#         if s3 == 5:
#             cnt += 1
#     # cnt가 3이상이면 빙고임
#     if cnt >= 3:
#         # 부른 횟수는 i+1임
#         print(i+1)
#         break
# print(called)