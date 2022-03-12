n = int(input())
numbers = map(int, input().split())  # 1 3 5 7
sosu = 0
for i in numbers:  # 1 3 5 7
    cnt = 0
    if i > 1 :
        for j in range(2, i):  # 2부터 n-1까지 2 3
            if i % j == 0:
                cnt += 1  # 2부터 n-1까지 나눈 몫이 0이면 cnt가 증가
        if cnt == 0:
            sosu += 1  # cnt가 없으면 소수.
print(sosu)