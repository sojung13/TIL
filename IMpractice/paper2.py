n = int(input())

result = set()
for _ in range(n):  # 3번동안 색종이 값 더할것임
    garo, sero= map(int,input().split())
    for i in range(garo, garo+10):  # 3부터 13까지! 그래프보면 사각형가로/세로는 정확히 13까지이다.
        for j in range(sero, sero+10):  # 7부터 17
            result.add((i,j))
print(len(result))