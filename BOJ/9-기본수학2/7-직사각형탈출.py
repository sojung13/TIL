x, y, w, h = map(int, input().split())
# 철수좌표 6,2 사각형 크기는 10,3
print(min(x, y, w-x, h-y))