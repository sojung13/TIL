n = int(input())  # 10

# for i in range(n, n*2+1):  # 10~20 사이 수
#     if i == 1: # 1은 소수가 아니므로 고잉
#         continue
#     for j in range(2, int(i** 0.5)+1 ):
#         if i%j==0:
#             break
#     else:
#         print(i)
아직 미완!!!!!!!!!!!!!!!!
sosu_list = []
for i in range(n, 2*n+1):  # 처음부터 끝 넘버까지
    cnt = 0
    if i > 1 :  # 2부터 시작
        for j in range(2, i):  # 2부터 i-1까지
            if i % j == 0:  # 나눈 값이 0이라면 cnt 추가
                cnt += 1
                break  
        if cnt == 0:
            sosu_list.append(i)  # cnt가 없으면 소수리스트에 추가
print(sosu_list.count())