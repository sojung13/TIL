import sys
sys.stdin = open('input.txt','r')

n = int(input())
for i in range(n):
    num = str(i)
    numb = 0
    for j in num:
        numb += int(j)
print(numb)






# 분해합 구하는 공식
# n = str(input())  # 2 1 6
# li = []
# result = 0
# result += int(n)
# for i in n:  # 216+2+1+6
#     li.append(i)   # 2 1 6
# result += int(i)
# print(result)