import sys
sys.stdin = open('input.txt','r')

day, term = map(int, input().split())
tem = list(map(int, input().split()))  # [3, -2, -4, -9, 0, 3, 7, 13, 8, -3]
count = 0
res = []
result = 0
re = []
for i in range(len(tem)):
    res.append(tem[i:i+term])   #[[3, -2], [-2, -4], [-4, -9], [-9, 0], [0, 3], [3, 7], [7, 13], [13, 8], [8, -3], [-3]]
    for j in res:  # j는 여기서 [3,-2] [-2,-4] 각각을 의미
        if len(j) == term:  # 만약 j의 길이가 term과 같다면(그보다 적은 애들 소거)
            result = sum(j)
            re.append(result)
print(max(re))

