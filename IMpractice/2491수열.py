# n = int(input())
# li = list(map(int,input().split()))
# count = 1
# lif = li[0]
# for i in range(n-1):
#     if li[i] >= li[i+1]:
#         count += 1
#     else:
#         count = 1

#     if li[i] <= li[i+1]:
#         count += 1
#     else:
#         count = 1
# print(count)

n = int(input())
li = list(map(int,input().split())) # 1 2 2 4 4 5 7 7 2 총 9개
cnt1 = 1
count = 1
for i in range(1,n):   # 오름차순으로 올라갈 경우
    if li[i-1] >= li[i]:  # 비교했을 때 점점 커지거나 같을 경우
        cnt1 += 1  # cnt1에 횟수 추가
    else:  
        cnt1 = 1
    if count < cnt1:  # 값 비교!!!!
        count = cnt1
cnt2 = 1   # 반대로 내림차순으로 차곡차곡 내려가거나 같은지 똑같이
for i in range(1,n):
    if li[i-1] <= li[i]:
        cnt2 += 1
    else:
        cnt2 = 1
    if count < cnt2:
        count = cnt2
print(count)




# 석현님 코드
# arr내 숫자 앞뒤값을 비교를 해서 count에 횟수 누적을 하되,
# 그 길이 숫자를 리스트에 넣어 그 중 가장 큰 값을 프린트하였습니다.
length = int(input())
arr = list(map(int, input().split()))
count_arr = []
count = 1
for i in range(1, len(arr)):
    if arr[i] >= arr[i-1]:
        count+= 1
    else:
        count = 1
count_arr.append(count)  

# count2 = 1
for i in range(1, len(arr)):
    if arr[i] <= arr[i-1]:
        count+= 1
    else:
        count = 1
count_arr.append(count)

# edge case
print(max(count_arr))

# 희원님 코드
# index 0 에는 점점 커지는 수열
# index 1 에는 점점 작아지는 수열
current_len = [1, 1] # 현재 수열의 길이
max_len = [1, 1] # 최대 수열의 길이
N = int(input())
nums = list(map(int, input().split()))
for i in range(1, N):
    if nums[i] > nums[i - 1]: # 이전 숫자가 더 작을 때
        # 점점 커지는 수열
        current_len[0] += 1
        # 점점 작아지는 수열
        max_len[1] = max(max_len[1], current_len[1])
        current_len[1] = 1
    elif nums[i] < nums[i - 1]: # 이전 숫자가 더 클 때
        # 점점 커지는 수열
        max_len[0] = max(max_len[0], current_len[0])
        current_len[0] = 1
        # 점점 작아지는 수열
        current_len[1] += 1
    else: # 이전 숫자와 같을 때
        # 점점 커지는 수열
        current_len[0] += 1
        # 점점 작아지는 수열
        current_len[1] += 1
max_len[0] = max(max_len[0], current_len[0])
max_len[1] = max(max_len[1], current_len[1])
print(max(max_len[0], max_len[1]))

# 근혜님 코드
N = int(input())
lst = list(map(int, input().split()))

b_lst = []
s_lst = []
b_cnt = s_cnt = 1
for i in range(N-1):
    # 커지는 숫자의 길이
    if lst[i+1] >= lst[i]:
        b_cnt += 1
    else:
        b_lst.append(b_cnt)  # 앞 숫자보다 작은 숫자가 나오는 경우 빈 리스트에 값을 추가
        b_cnt = 1

    # 작아지는 숫자의 길이
    if lst[i+1] <= lst[i]:
        s_cnt += 1
    else:
    # 마찬가지로 반대의 경우가 나오면 리스트에 그 값을 추가해주었습니다.
        s_lst.append(s_cnt)
        s_cnt = 1

    # 추가) 마지막 인덱스의 값도 포함되도록
    if i+1 == N-1:
        b_lst.append(b_cnt)
        s_lst.append(s_cnt)

# 그 중 제일 긴 길이
total_lst = b_lst + s_lst
result = max(total_lst)
print(result)