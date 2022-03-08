import sys
sys.stdin = open('sample_input.txt','r')

t = int(input())
for tc in range(1, t+1):
    n = int(input())  # 6
    li = list(input().split())  # a b c d e f

    st_idx1 = 0
    st_idx2 = (n+1)//2
    print(f'#{tc}', end='')
    for i in range(st_idx2):
        print(li[st_idx1 + i], end='')
        if st_idx2 + i < n:
            print(li[st_idx2 + i], end='')
    print()
    # result = [''] * n
    # for i in range(len(li)):  # 6
    #     if i%2:
    #         result[i] += li[i]
    #     else:
    #         result[i-1] += li[i-1]
    # print(f'#{tc} {result}')