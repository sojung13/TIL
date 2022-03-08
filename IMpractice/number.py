n = int(input())  # 9
number = list(map(int,input().split()))
li = []

for i in range(n):   #9
    max_count = 1
    min_count = 1
    if number[i] <= number[i+1]:
        max_count += 1
    elif number[i] >= number[i+1]:
        min_count += 1
    else:
        break

print(max(max_count, min_count))