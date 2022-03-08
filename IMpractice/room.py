student, max_num = map(int,input().split())   # 16명인데 각 방 2명씩.

for i in range(student):  # student 수 16만큼 출력.
    gender, grade = map(int,input().split())  # 성별과 학년 입력
    result = 0   # +=1 해줄 값
    for i in gender:    # gender 0과 1로 구성
        for j in grade:   # grade 1부터 6까지
            if 

print(result)


# 여기서부터 코드 리뷰 분석 - 희원님 # 

student, max_num = map(int, input().split())
rooms = [[0 for i in range(2)] for j in range(6)]  # 2* 6 matrix
for i in range(student):  # N명 만큼 돌아야한다.
    gender, grade = map(int,input().split())  # 성별, 학년 숫자 받고
    rooms[grade-1][gender] += 1 
# grade에서 -1을 해주는 이유는 grade 숫자가 1부터 시작하기 때문.
# 인덱스는 0에서부터 시작하기 때문에 -1해줘서 인덱스를 맞춰준다.

# 일단 방 최대 인원수 생각 안해주고 2*6 matrix인 rooms에 모든 인원 다 넣어준다.


# 방 카운트할 변수 설정
count = 0
for i in range(6):
    for j in range(2):    # for문 두 번 써서 사각형 틀 만들긔!
        if rooms[i][j] % max_num:   # 인원이 max_num 보다 많을 때
            count += rooms[i][j] // max_num + 1  # max_num으로 나눠주고 +1
        else:    # 인원이 딱 맞아떨어질때
            count += rooms[i][j] // max_num
print(count)   # 방 갯수만큼 +1된 값을 프린트해준다.



#  동현님 코드
N, K = map(int, input().split())
li_y0 = []
li_y1 = []
cnt_0 = 0
cnt_1 = 0
for _ in range(N):
    S , Y = map(int, input().split())  # 남학생, 여학생 수 받기
    # 여학생 일때 
    if S == 0:
        li_y0.append(Y)
    # 남학생 일때
    else:
        li_y1.append(Y)    

# 학년을 구분
for i in range(1, 7):
    # 여학생 리스트에서
    if li_y0.count(i) >=1:
        # 나눗셈이 딱 맞아 떨어질때
        if li_y0.count(i)%K == 0:
            y0 = li_y0.count(i)//K
            cnt_0 += y0
        # 나머지가 남으면
        else:
            y0 = (li_y0.count(i)//K +1)
            cnt_0 += y0
# 학년을 구분
for i in range(1, 7):
    # 남학생 리스트에서
    if li_y1.count(i) >=1:
        # 나눗셈이 딱 맞아 떨어질때
        if li_y1.count(i)%K == 0:
            y1 = li_y1.count(i)//K
            cnt_1 += y1
        # 나머지가 남으면
        else:
            y1 = (li_y1.count(i)//K +1)
            cnt_1 += y1
        
print(cnt_0+cnt_1)


#  근혜님 코드

N, K = map(int, input().split())
students_lst = [list(map(int, input().split())) for student in range(N)]

# 남녀 방 나누기 & 모든 방을 [0]으로 설정
room_girl = [[0] for _ in range(6)]  # 12개의 각 방은 0으로 구성되어 있다
room_boy = [[0] for _ in range(6)]

# 성별별 학년 분류
for i in range(N) :
    for j in range(1,7):  # 1~6
        if students_lst[i][0] == 0 and students_lst[i][1] == j:   # 여자면서 학년 같으면
            room_girl[j-1][0] += 1  # 1명씩 넣어준다

        elif students_lst[i][0] == 1 and students_lst[i][1] == j:   # 남자면서 학년 같으면
            room_boy[j-1][0] += 1

# 빈 방 제외
cnt_girl = 6
cnt_boy = 6
for i in range(6):
    if room_girl[i] == [0]:
        cnt_girl -= 1
for i in range(6):
    if room_boy[i] == [0]:
        cnt_boy -= 1

# 각 방 학생 수가 최대인원수를 넘으면 방 추가
# if문 써서 나머지가 0일 때와 아닐 때로 구분하려다가 좀더 간단하게 하기 위해 ceil 사용
import math
total_room = 0
for i in range(6):
    if room_girl[i][0] > K:
        cnt_girl += math.ceil(room_girl[i][0]/K)-1
for i in range(6):
    if room_boy[i][0] > K:
        cnt_boy += math.ceil(room_boy[i][0]/K)-1

total_room = cnt_girl + cnt_boy
print(total_room)

