import sys
sys.stdin = open('input.txt','r')

def check():
    # 가로행
    for r in range(9):
        cnt = [0] * 10
        for c in range(9):
            t = arr[r][c]
            if cnt[t] == 1:
                return 0
            cnt[t] = 1

    # 세로열
    for r in range(9):
        cnt = [0] * 10
        for c in range(9):
            t = arr[c][r]
            if cnt[t] == 1:
                return 0
            cnt[t] = 1

    for stR in range(0,9,3):
        for stC in range(0,9,3):
            cnt = [0] * 10
            for r in range(3):
                for c in range(3):


# n = int(input())
# for tc in range(1,n+1):
#     arr = [list(map(int,input().split())) for _ in range(9)]
#
#     for r in range(9):
#         for c in range(8):
#             if arr[r][c] != arr[r][c+1]:
#                 result = 1
#             else:
#                 result = 0
#
#     for r in range(8):
#         for c in range(9):
#             if arr[c][r] != arr[c][r+1]:
#                 result = 1
#             else:
#                 result = 0
#
#     for r in range(9):
#         for c in range(9):
#             if arr
#     print(f'#{tc} {result}')


