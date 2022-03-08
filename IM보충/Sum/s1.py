import sys
sys.stdin = open('input.txt','r')

for tc in range(1,11):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    maxV = 0
    # 가로값
    for r in range(len(arr)):
        count = 0
        for c in range(len(arr)):
            count += arr[r][c]
            if count > maxV:
                maxV= count
    # 세로값
    for r in range(len(arr)):
        count = 0
        for c in range(len(arr)):
            count += arr[c][r]
            if count > maxV:
                maxV = count
    # 대각선값
    countx = 0
    for i in range(100):
        countx += arr[i][i]
    if countx > maxV:
        maxV = countx
    # 반대 대각선값
    countx = 0
    for i in range(100):
        countx += arr[i][99-i]
    if countx > maxV:
        maxV = countx

    print(f'#{tc} {maxV}')
