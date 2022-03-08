n = int(input())
count = 0
if n % 5 == 3:  # 만약 5로 나누고 나머지가 3의 배수와 일치할 때
    count += 1
elif n % 3 == 5:
    count += 1
else:  # 어떤 경우로도 나눠질 수 없을때
    count = -1
print(count)