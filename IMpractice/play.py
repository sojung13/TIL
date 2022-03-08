n = int(input())

for i in range(n):    # 게임 n번동안 플레이함
    a= list(map(int,input().split()))   # a랑 b의 딱지 패턴
    b= list(map(int,input().split()))
    a.pop(0)  # 주어지는 숫자 배열 중 맨 앞은 갯수 표시라 없앤다
    b.pop(0)
    for j in range(4, 0, -1):   # 4인 별모양이 가장 큰 포인트를 주기 때문에 4부터 시작, 1까지 간다.
        if a.count(j) > b.count(j):
            print('A')
            break
        elif a.count(j) < b.count(j):
            print('B')
            break
    else:
        print('D')

# for i in range(n):   # 게임 n번동안 플레이함
#     count_a = 0
#     count_b = 0
#     for j in a:
#         count_a += j
#     for k in b:
#         count_b += k
#     # a의 합산과 b의 합산 값을 구함
#     if count_a > count_b:
#         print('A')
#     elif count_a < count_b:
#         print('B')
#     else:
#         print('D')

for _ in range(n):  # 게임 n번동안 플레이함
    a= map(int,input().split())   # a랑 b의 딱지 패턴
    b= map(int,input().split())
    a.pop(0)
    b.pop(0)
    if a.count(4) > b.count(4):  
        print('A')
    elif a.count(4) < b.count(4):
        print('B')
    # elif a.count(4) == b.count(4):
    else:
        if a.count(3) > b.count(3):
            print('A')
        elif a.count(3) < b.count(3):
            print('B')
        elif a.count(3) == b.count(3):
            if a.count(2) > b.count(2):
                print('A')
            elif a.count(2) < b.count(2):
                print('B')
            elif a.count(2) == b.count(2):
                if a.count(1) > b.count(1):
                    print('A')
                elif a.count(1) < b.count(1):
                    print('B')
                elif a.count(1) == b.count(1):
                    print('D')



#  희원님 코드
import sys
N = int(input())
for i in range(N):  # 빠른 비교를 위해 import sys
    _, *shape_A = map(int, sys.stdin.readline().strip().split())
    _, *shape_B = map(int, sys.stdin.readline().strip().split())
    for i in range(4, 0, -1):   # 4에서부터 거꾸로 세어준다(4인 별이 가장 중요하기때문)
        if shape_A.count(i) > shape_B.count(i):
            print('A')
            break
        elif shape_A.count(i) < shape_B.count(i):
            print('B')
            break
    else:
        print('D')



# 동현님 코드
# 라운드 수
N = int(input())

for i in range(N):
    # A와 B 입력
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 카운트로 비교
    # pop 대신 [:]값으로 i번째 이후의 모든 값들로 처리
    # 4,3,2,1 순으로 더 큰 값을 비교 후 출력
    if A[1:].count(4) > B[1:].count(4):
        print('A')
    elif A[1:].count(4) < B[1:].count(4):
        print('B')
    else:
        if A[1:].count(3) > B[1:].count(3):
            print('A')
        elif A[1:].count(3) < B[1:].count(3):
            print('B')
        else:
            if A[1:].count(2) > B[1:].count(2):
                print('A')
            elif A[1:].count(2) < B[1:].count(2):
                print('B')
            else:
                if A[1:].count(1) > B[1:].count(1):
                    print('A')
                elif A[1:].count(1) < B[1:].count(1):
                    print('B')
                else:
                    print('D')


# 근혜님 코드
N = int(input())
AB_lst = [list(map(int, input().split())) for i in range(2*N)]

# 1,2,3,4 개수 세어서 딕셔너리로 만들어놓고 요소끼리 비교
dict_lst = []
for i in AB_lst:
    a = i.count(4)
    b = i.count(3)
    c = i.count(2)
    d = i.count(1)
    elm = {'4':a,'3':b,'2':c,'1':d}
    dict_lst += [elm]

# 4,3,2,1 순으로 세어주며 출력
# 위에 리스트 값을 한번에 받아서 홀짝 개념으로 비교
for i in range(N):
    if dict_lst[2*i].get('4') > dict_lst[2*i+1].get('4'):        
        print('A')
    elif dict_lst[2*i].get('4') < dict_lst[2*i+1].get('4'):
        print('B')
    else:
        if dict_lst[2*i].get('3') > dict_lst[2*i+1].get('3'):
            print('A')
        elif dict_lst[2*i].get('3') < dict_lst[2*i+1].get('3'):
            print('B')
        else:            
            if dict_lst[2*i].get('2') > dict_lst[2*i+1].get('2'):
                print('A')
            elif dict_lst[2*i].get('2') < dict_lst[2*i+1].get('2'):
                print('B')
            else:
                if dict_lst[2*i].get('1') > dict_lst[2*i+1].get('1'):
                    print('A')
                elif dict_lst[2*i].get('1') < dict_lst[2*i+1].get('1'):
                    print('B')
                else:
                    print('D')