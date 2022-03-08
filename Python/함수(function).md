## 함수

> 함수의 정의

- 특정한 기능을 하는 코드의 조각(묶음)
- 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, `필요 시`에만 호출하여 간편히 사용
- ![image-20220119094816478](함수(function).assets/image-20220119094816478.png)



개발자들의 금단의 함수 ^,^ = max(), min()

- 사용자 함수 (Custom Function)
  - 구현되어 있는 함수가 없는 경우, 사용자가 직접 함수를 작성 가능



> 선언과 호출(define & call)

- 함수의 선언은 def 키워드를 활용함
- 들여쓰기를 통해 Function body(실행될 코드 블록)를 작성함
  - Docstring은 함수 body 앞에 선택적으로 작성 가능
    - 작성시에는 반드시 첫 번째 문장에 문자열 ''' '''
- 함수는 parameter를 넘겨줄 수 있음
- 함수는 동작 후에 return을 통해 결과값을 전달함

- 함수는 함수명()으로 호출
  - parameter가 있는 경우, 함수명(값1, 값2, ...)로 호출
- 함수는 호출되면 코드를 실행하고 return 값을 반환하며 종료된다!!!

![image-20220119092243634](함수(function).assets/image-20220119092243634.png)



```python
# 숫자를 받아서 (input)
# 세제곱 결과를 반환  (output)
# 호출 : cube(2), cube(10), cube(100)

def cube(number):
	return number * number * number

print(cube(2))
```

= 8 (2의 3승이기 때문)



> 주의 - return vs print

- return : 함수 안에서만 사용되는 키워드
- print : 출력을 위해 사용되는 함수
- REPL( Read - Eval - Print Loop ) 환경에서는 마지막으로 작성된 코드의 리턴 값을 보여주므로 같은 동작을 하는 것으로 착각할 수 있음

![image-20220119202205697](함수(function).assets/image-20220119202205697.png)



> 두 개 이상의 값 반환

```python
def minus_and_product(x, y):
    return x - y
	return x * y

print(minus_and_product(1,2))
```

이렇게 하면 return 값을 하나만 출력하기 때문에 첫 번째인 x - y 의 값 -1을 출력한다!

```python
def m(x, y):
    return x - y, x * y

a = m(4,5) 
print(a)

print(type(a))
```

(-1, 20) 값을 반환한다. 여기서 타입은 튜플이다!!!!!!!





> 사각형 넓이, 둘레길이 구하기

```python
def rectangle(width, height):
    return width * height, (width + height) * 2

print(rectangle(30,20))
#=> (600, 100) 하나의 튜플이다!!!
```



> Parameter 와 Argument

- Parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자
- Argument : 함수를 호출할 때, 넣어주는 값
  - 함수 호출 시 함수의 parameter를 통해 전달되는 값
  - Argument는 소괄호 안에 할당 func_name(argument)
    - 필수 Argument : 반드시 전달되어야 하는 argument
    - 선택 Argument : 값을 전달하지 않아도 되는 경우는 기본 값이 전달



![image-20220119102741596](함수(function).assets/image-20220119102741596.png)





> Positional Arguments Packing/ Unpacking

- Positional Arguments Packing/ Unpacking 연산자(*)
  - 여러 개의 positional Arguments를 하나의 필수 Parameter로 받아서 사용
- 언제 사용하는가?
  - 몇 개의 Positional Arguments를 받을지 모르는 함수를 정의할 때 유용

```python
print('hi', 'hello', '안녕', 'Guten Morgen', 'Bon jour')

def add(*args):
    print(args, type(args))
    return sum(args)
    
add(1,2,3)
add
```





>  Keyword Arguments Packing/ Unpacking

- Keyword Arguments Packing/ Unpacking 연산자(**)
  - 함수가 임의의 개수 Argument를 keyword Argument로 호출될 수 있도록 지정
  - Argument들은 딕셔너리로 묶여 처리되며, parameter에 **를 붙여 표현

```python
def family(**kwagrs):
    print(kwagrs, type(kwagrs))
    
family(father='고길동', monster='둘리')
```

{'father':'고길동', 'monster':'둘리'}    <class 'dict'>



### 함수의 범위(Scope)

![image-20220119110755761](함수(function).assets/image-20220119110755761.png)

함수는 이 그림 하나로 설명이 가능하다!!!!!

- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
- scope
  - global scope : 코드 어디에서든 참조할 수 있는 공간
  - local scope : 함수가 만든 scope. 함수 내부에서만 참조 가능
- variable
  - global variable : global scope에 정의된 변수
  - local variable : local scope에 정의된 변수



```python
def ham():
    a = 'spam'
	return a
print(a)   #NameError: name 'a' is ont defined

# 함수는 가장 기본 : local scope!
# 블랙박스의 결과를 받아보고 싶으면 반환 값을 변수에 저장해서 사용하는 것!
# 블랙박스 밖으로 결과를 주고 싶을 수 있어요! => return 해야해요
```



> 변수 수명주기(lifecycle)

- 변수는 각자의 수명주기(lifecycple)가 존재
  - built-in scope
    - 파이썬이 실행된 이후부터 영원히 유지
  - global scope
    - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
  - local scope
    - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지



> 이름 검색 규칙(Name Resolution)

- 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음
- 아래와 같은 순서로 이름을 찾아나가며, LEGB Rule이라고 부름
  - Local scope : 함수
  - Enclosed scope : 특정 함수의 상위 함수
  - Global scope : 함수 밖의 변수, Import 모듈
  - Built-in scope : 파이썬 안에 내장되어 있는 함수 또는 속성

![image-20220119204802293](함수(function).assets/image-20220119204802293.png)



```python
a = 0
b = 1
def enclosed():
    a = 10
    c = 3
    def local(c):
        print(a, b, c)    # (10, 1, 300)
    local(300)
    print(a, b, c)		  # (10, 1, 3)
enclosed()
print(a, b)    			  # (0,1)
```





![image-20220119112858909](함수(function).assets/image-20220119112858909.png)



> global 문

현재 코드 블록 전체에 적용되며, 나열된 식별자(이름)이 global variable임을 나타냄

- global에 나열된 이름은 같은 코드 블록에서 global 앞에 등장할 수 없음
- global에 나열된 이름은 parameter, for 루프 대상, 클래스/ 함수 정의 등으로 정의되지 않아야 함



> nonlocal

global을 제외하고 가장 가까운(둘러싸고 있는) scope의 변수를 연결하도록 함

- nonlocal에 나열된 이름은 같은 코드 블록에서 nonlocal 앞에 등장할 수 없음
- nonlocal에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함

global과는 달리 이미 존재하는 이름과의 연결만 가능함



> Naming Convention

- 좋은 함수와 parameter 이름을 짓는 방법
  - 상수 이름은 영문 전체를 대문자
  - 클래스 및 예외의 이름은 각 단어의 첫 글자만 영문 대문자
  - 이외 나머지는 소문자 또는 밑줄로 구분한 소문자 사용 > 함수

- 스스로를 설명
  - 함수의 이름만으로 어떠한 역할을 하는 함수인지 파악 가능해야 함
  - 어떤 기능을 수행하는지, 결과 값으로 무엇을 반환하는지 등
- 약어 사용을 지양
  - 보편적으로 사용하는 약어를 제외하고 가급적 약어 사용을 지양

개발자들에게 네이밍이란 숙명과도 같은 것이다!!!!!!!



> map(function, iterable)

순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function) 적용하고 그 결과를 map object로 반환



> filter(function, iterable)

순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function) 적용하고 그 결과가 True인 것들을 filter object로 반환



> zip(*iterables)

복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환



> lambda 함수

표현식을 계산한 결과값을 반환하는 함수로, 이름이 없는 함수여서 `익명함수`라고도 불림

- return 문을 가질 수 없음
- 간편 조건문 외 조건문이나 반복문을 가질 수 없음
- 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
- def를 사용할 수 없는 곳에서도 사용 가능



> 재귀 함수(recursive function)

- 자기 자신을 호출하는 함수
- 무한한 호출을 목표로 하는 것이 아니며, 알고리즘 설계 및 구현에서 유용하게 활용
  - 알고리즘 중 재귀 함수로 로직을 표현하기 쉬운 경우가 있음(예 - 점화식)
  - 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
- 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성
- 대표적인 것이 팩토리얼(!)



> 반복문과 재귀 함수의 비교

- 알고리즘 자체가 재귀적인 표현이 자연스러운 경우 재귀함수 사용
- 재귀 호출은 변수 사용을 줄여줄 수 있음
- 재귀 호출은 입력 값이 커질수록 연산 속도가 오래 걸림

