for i in range(4):
    x1,y1,x2,y2,a1,b1,a2,b2 = list(map(int,input().split()))
    rec_xy = [x1, y1, x2, y2]
    rec_ab = [a1, b1, a2, b2]
    result = ''
    if max(rec_xy) < min(rec_ab):
        result = 'd'
    elif

    else:

    print(result)

    # for x in rec_xy:
    #     for a in rec_ab:
    # # 만약 첫번째 사각형의 큰 좌표점이 두번째 사각형의 작은 좌표점보다 작으면
    # # 이 두 사각형은 겹치지 않은 형태가 된다.
    #         if max(rec_xy) < min(rec_ab):
    #             result = 'd'
    # # 만약 좌표점 중에 한 값이 겹치게 되면
    # # 이 두 사각형은 선분으로 겹치는 형태인 것이다.
    #         elif x == a:
    #             count += 1
    #             if count == 1:
    #                 result = 'b'
    # # 만약 좌표점 중 두 값이 겹치게 되면
    # # 점으로 완전히 겹치게 되는 형태다.
    #             else:
    #                 result = 'c'
    #         else:
    #             result = 'a'
    # print(result)
