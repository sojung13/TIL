# real_dwarf = []   # 진짜 난쟁이 찾아줄 리스트 구한다.
# fake_dwarf = []
# total = 0

# # for _ in range(1,10):   # 난쟁이 수가 9명이기 때문에 9명 돈다
# dwarf = list(map(int,input().split()))   # dwarf들 값 입력!
# for i in dwarf:  # i는 dwarf 9명의 모든 키 값들
#     total += i  # 여기서 total은 무조건 100 이상 값이다. 140
#     extra = total - 100  # 40
#         # 만약 난쟁이 두 명의 합이 extra인 40이라면
#         # 그 두명을 제외한 나머지 7명의 값을 빈 리스트에 넣어주자.
    


# 9명의 값들을 다 더해주고,
# 100보다 오버된 값만큼 더한 애들을 뺴준다.
# 남은 애들을 real_dwarf안에 넣어주자.


dwarf = [int(input()) for _ in range(9)]
total = 0
for k in dwarf:
    total += k   # 140
    extra = total - 100   # 40
for i in range(len(dwarf)):
    for j in range(len(dwarf)):
        if dwarf[i] + dwarf[j] == extra:
            dwarf.pop(i)
            dwarf.pop(j)
            break
    else:
        break
    print(dwarf)

