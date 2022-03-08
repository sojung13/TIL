# import sys
# sys.stdin = open('input.txt','r')
#
# t = int(input())
# for tc in range(1, t+1):
#     n,m,k = map(int,input().split())  # n명의 사람 m초의 시간 k개의 붕어빵
#     person = list(map(int,input().split()))
#     person.sort()
#     result = 'Possible'
#     for i in range(n):
#         t = person[i]//m + k
#         if t < (i+1):
#             result = 'Impossible'
#             break
#
#     print(f'#{tc} {result}')

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    # N 손님 수 M 초마다 K개 생산
    N,M,K = map(int,input().split()) # 2 2 2
    lst = list(map(int,input().split())) # 몇초에 오는지 # 3 4

    lst.sort() # 몇초에 오는지 정렬해놓고 시작
    # print(lst)

    붕어빵리스트 = [0 for i in range(lst[-1]+1)]
    붕어빵 = 0

    # 붕어빵 리스트 만들기
    for i in range(len(붕어빵리스트)): # 0 1 2 3 4
        if i % M == 0 and i != 0: # 2초마다
            붕어빵 += K  # 붕어빵 만들어지는 횟수 과정
        붕어빵리스트[i] = 붕어빵  # 붕어빵 만들어지는 과정 리스트로 도식화
    # print(붕어빵리스트)

    # 손님 오세요
    for j in lst : # 3 4
        for i in range(j,len(붕어빵리스트)) :
            붕어빵리스트[i] -= 1  # 손님이 사갈때마다 붕어빵 진열대에서 1개씩 없어짐

    # print(붕어빵리스트)

    # 그 과정 속에서 한 번이라도 붕어빵이 바닥난적이 있다면 Impossible
    for i in 붕어빵리스트 :
        if i >= 0 :
            result = 'Possible'
        else :
            result = 'Impossible'
            break

    print(f'#{tc} {result}')