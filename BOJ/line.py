n = int(input())
student = list(map(int,input().split()))
result = []

for i in range(n):   # 5번 돌아간다
    result.insert(student[i],i+1)
print(*result[::-1])



# 5번 돌려서 > 리스트 숫자 일단 받고 > 앞에서부터 받은 숫자 j 값만큼
# 인덱스 넘버를 마이너스 시켜준다.
# 빈 리스트에 오리지날 인덱스 넘버를 append 해준다..? 뭔가 append 해야할 삘인데
