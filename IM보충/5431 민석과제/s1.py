import sys
sys.stdin = open('input.txt','r')

t = int(input())
for tc in range(1,t+1):
    n , k = map(int,input().split()) # n= 전체 수강생 k = 과제낸사람수
    li = list(map(int,input().split()))  # 과제낸 사람 인덱스
    res = [i + 1 for i in range(n)]  # [1, 2, 3, 4, 5]
    for j in li:  # 2 5 3
        if res[j-1] == j:
            res.pop(j)
    print(res)


