import sys
sys.stdin = open('input.txt','r')

n, m = map(int,input().split())
cards = list(map(int,input().split()))
li = []

for i in range(len(cards)):
    for j in range(i+1,len(cards)):
        for k in range(j+1,len(cards)):
            if cards[i] + cards[j] + cards[k] <= m:
                li.append(cards[i] + cards[j] + cards[k])
            else:
                continue
print(max(li))