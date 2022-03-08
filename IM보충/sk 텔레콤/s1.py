import sys
sys.stdin = open('input.txt','r')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(input()) for _ in range(n+1)]

    for r in range(n):
        for c in range(n):
            if arr[r][c] == 'X' or arr[r][c] == 'm':
                continue
            if arr[r][c] == 'A':
                k = 1
            if arr[r][c] == 'B':
                k = 2
            if arr[r][c] == 'C':
                k = 3
            for i in range(1, k+1):
                # 상
                if r-i>=0 and arr[r-i][c] =='m':
                    arr[r][c] ='o'
                # 하
                # 좌
                # 우
    cnt = 0
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 'm':
                cnt += 1
    print(cnt)
