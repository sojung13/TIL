n = int(input())   # 5
student = list(map(int,input().split()))  # 0 1 1 3 2
result = []

for i in range(n):   # 0 1 2 3 4
    result.insert(i-student[i], i+1)  # ex. 2-1,2+1
print(result)

