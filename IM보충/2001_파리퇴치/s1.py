import sys
sys.stdin = open('input.txt','r')

t= int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    maxV = 0
    for sr in range(n-m+1):
        for sc in range(n-m+1):
            count = 0
            for r in range(m):
                for c in range(m):
                    count += arr[sr+r][sc+c]
                if count > maxV:
                    maxV = count
    print(f'#{tc} {maxV}')
