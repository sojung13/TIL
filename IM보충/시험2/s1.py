import sys
sys.stdin = open('algo2_sample_in.txt','r')

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    count = 0
    count2 = 0
    dr = [0,0,-1,1]  # 좌 우 상 하
    dc = [-1,1,0,0]
    # for i in range(n-1):
    #     for j in range(n-1):
    #         for r in range(3):
    #             for c in range(3):

    for r in range(n):
        for c in range(n):
            count += arr[r][c]



            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < n and 0 <= nc < n:
                    count2 += arr[nr][nc]
    if count > count2:
        result = count
    else:
        result = count2
    print(f'#{tc} {result}')
