# 1. while의 try / except :
while True:
    try:
        a,b= map(int,input().split())
        print(a + b)
    except:
        break

# 2. 혹시 for문과 while문을 특별히 구분해서 작성하는 경우가 있는지??
# while보다도 for문을 더 자주 보는 것 같은데, while을 써야하는 경우에
# while True로 작성하는 형태도 보편적인 것인지

# 3. sys.stdin.readline()의 의미와 역할
# 위의 sys와 밑의 input의 차이?
import sys

T = int(input())

for i in range(1, T + 1):
    A, B = map(int,sys.stdin.readline().split())
    print(A + B)

T = int(input())

for i in range(1, T + 1):
    A, B = map(int,input().split())
print(A + B)  > 시간초과가 뜬다!!


# 4. for _ in range(n):
_가 값을 무시하고 싶을때 사용하여 주로 인덱스가 필요하지 않을때 간단히 쓰인다고 하는데,
for i in range(n)처럼 i가 n-1까지의 숫자들을 다 도는 것과
어떤 차이점이 있는지???? 값을 불러오는 것에서??


# 5. 재귀함수
# 정해진 문법?이 아니라 만드는 양식의 차이??
n = int(input())

result = 1
if n > 0:
    for i in range(1, n+1):
        result *= i
print(result)


def countdown(n):
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)

# 6. IM의 난이도,,,
# 백준으로 치면 브론즈 수준인지 실버 or 골드수준인지 궁금합니다,,