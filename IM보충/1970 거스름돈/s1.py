import sys
sys.stdin = open('input.txt','r')
mon = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
n = int(input())
for tc in range(1, n+1):
    money = int(input())
    result = [0 for _ in range(8)]
    for i in range(len(mon)):
        result[i] = money//mon[i]
        money = money%mon[i]
    print(f'#{tc}')
    print(*result)