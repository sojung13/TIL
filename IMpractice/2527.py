for _ in range(4):
    x1, y1, x2, y2, a1, b1, a2, b2 = map(int,input().split())
    rec_xy = [x1, y1, x2, y2]
    rec_ab = [a1, b1, a2, b2]

# x2 - x1= ex. 9-3=6 이므로 첫번째 사각형의 가로길이는 6이다
# x1, x2, a1, a2 는 각각 가로길이를 출력해줄 값들
# y1, y2, b1, b2 는 각각 세로길이를 출력해줄 값들


# # 직사각형인 경우 A
# 
            # if (x2-a2 > 0 and y2-b2 > 0) or (a2-x2>0 and b2-y2>0):
            #     # if (x2-a2 > 0 and y2-b2 <0) or (a2-x2>0 and b2-y2<0):
            #     print("a")
            #  xy 사각형이 먼저 나오는 경우:
    if x2 > a1 and y2 > b1:
        if (x2 - a1) > 0 and (y2-b1) > 0:
            print("a")

# # 만약 선으로 맞닿는 경우 B
# # 각 값들 중 하나의 좌표값만이 동일할때 선상이다
    for i in range(len(rec_xy)):
        for j in range(len(rec_ab)):
            count = 0            
            
            if rec_xy[i] == rec_ab[j]:
                count += 1
                if count == 1:
                    print("b")

# # 만약 점인 경우 C
# # 각 사각형 xw와 ab의 꼭짓점의 좌표 (a,b) 하나만 동일할 때
# xy와 ab에 속한 4값 중 2값이 겹치면 좌표값이 맞닿는 것

            # if rec_xy[i] == rec_ab[j]:
            #     count += 1
                elif count == 2: 
                    print("c")
                
# # 만약 공통부분이 없을 경우 D
# 한 사각형의 최댓값이 다른 사각형의 최솟값보다 적으면 완전히 다른 범위임
    # if max(rec_xy) < min(rec_ab) or max(rec_ab) < min(rec_xy):
        print("d")
