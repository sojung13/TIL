start, end = map(int, input().split())  # 3부터 16까지

for i in range(start, end+1):  # 3~16
    if i == 1: # 1은 소수가 아니므로 고잉
        continue
    for j in range(2, int(i** 0.5)+1 ):
        if i%j==0:
            break
    else:
        print(i)