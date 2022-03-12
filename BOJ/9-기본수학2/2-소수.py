start_num = int(input())  # 60
last_num = int(input())   # 100

sosu_list = []
for i in range(start_num, last_num+1):  # 처음부터 끝 넘버까지
    cnt = 0
    if i > 1 :  # 2부터 시작
        for j in range(2, i):  # 2부터 i-1까지
            if i % j == 0:  # 나눈 값이 0이라면 cnt 추가
                cnt += 1
                break  
        if cnt == 0:
            sosu_list.append(i)  # cnt가 없으면 소수리스트에 추가
            
if len(sosu_list) > 0 :  # 첫째줄 합 반환 둘째줄 최솟값 반환
    print(sum(sosu_list))
    print(min(sosu_list))
else:  # 없으면 -1 반환
    print(-1)