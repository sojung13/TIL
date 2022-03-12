x_nums = []
y_nums = []
for _ in range(3):
    x, y = map(int, input().split())
    x_nums.append(x)  # x 좌표만 저장
    y_nums.append(y)  # y 좌표만 저장

# 각각의 정답 좌표는 혼자 존재하는 다른 좌표값과 페어를 맞춰야 한다!!
for i in range(3):
    if x_nums.count(x_nums[i]) == 1:
        x4 = x_nums[i]
    if y_nums.count(y_nums[i]) == 1:
        y4 = y_nums[i]
print(x4, y4)