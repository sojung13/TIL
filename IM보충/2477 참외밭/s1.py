import sys
sys.stdin = open('input.txt','r')

n = int(input())
for i in range(6):
    direction, meter = map(int,input().split())
