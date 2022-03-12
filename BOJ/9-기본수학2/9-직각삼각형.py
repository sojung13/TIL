while True:
    # 수 크기대로 일단 정렬시켜주기
    li = sorted(list(map(int, input().split())))
    if sum(li) == 0:  # 0이면 끝
        break
    if li[0]**2 + li[1]**2 == li[2]**2:  # a제곱 + b제곱= c 제곱
        print('right')
    else:
        print('wrong')