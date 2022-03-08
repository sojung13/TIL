import sys
sys.stdin = open('input.txt','r')

t = int(input())
idx = []
height = []
total = []
for tc in range(t):
    n, h = map(int,input().split())
    idx.append(n)  # [2, 11, 15, 4, 5, 8, 13]
    height.append(h)  # [4, 4, 8, 6, 3, 10, 6]
    total.append([n,h])  # [[2, 4], [11, 4], [15, 8], [4, 6], [5, 3], [8, 10], [13, 6]]
    place = [0] * (max(idx)+2)  # [0,0,0,.... 0]

    for i,j in total:
        place[i] = j   # [0, 0, 4, 0, 6, 3, 0, 0, 10, 0, 0, 4, 0, 6, 0, 8, 0]

    mmax = max(place)  # 높이 10인 빌딩
    mmmax = place.index(mmax)

    # 가장 큰 빌딩 전까지 차곡차곡 올라가기
    for k in range(mmmax-1):
        if place[k] > place[k+1]:
            place[k+1] = place[k]
    # [0, 0, 4, 4, 6, 6, 6, 6, 10, 0, 0, 4, 0, 6, 0, 8, 0]

    # 끝에서부터 가장 큰 빌딩 전까지 차곡차곡 역순으로 올라가기
    for l in range(len(place)-1,mmmax,-1):  # 16, 8, -1 : 16 15 14 13...
        if place[l] > place[l-1]:
            place[l-1] = place[l]

    result = sum(place)
print(result)
print(place)