import sys
sys.stdin = open('input.txt','r')

w, h = map(int,input().split())  # width, height
p, q = map(int,input().split())  # 처음 좌표값 x, y
n = int(input())   # 몇 번 움직이는지. 8번 움직임
x = y = 0

for i in range(n):
    p += 1
    q += 1
    if p == w:
        p -= 1
    if q == h:
        q -= 1


print(p)
