### 디버깅

"코드의 상태를 신중하게 출력해가며 심사숙고하는 것보다 효과적인 디버깅 도구는 없다."

- print문 활용 : 특정 함수 결과, 반복/ 조건 결과 등 나눠서 생각
- 개발 환경(text editior, IDE) 등에서 제공하는 기능 활용
- Python tutor 활용(단순 파이썬 코드인 경우)
- 뇌컴파일, 눈디버깅



> 문법 에러(Syntax Error)

- Syntax Error가 발생하면, 파이썬 프로그램은 실행이 되지 않음
- 파일이름, 줄번호, ^문자를 통해 파이썬이 코드를 읽어 나갈 때(parser) 발생한 위치를 표현
- 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿(caret) 기호(^)를 표시

![image-20220124214732289](에러,예외 처리(Error,Exception Handling).assets/image-20220124214732289.png)

![image-20220124214743180](에러,예외 처리(Error,Exception Handling).assets/image-20220124214743180.png)

![image-20220124214751188](에러,예외 처리(Error,Exception Handling).assets/image-20220124214751188.png)





> 예외(Exception)

- 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤
  - 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러
- 실행 중에 감지되는 에러들을 예외(Exception)라고 부름
- 예외는 여러 타입(Type)으로 나타나고, 타입이 메세지의 일부로 출력됨
  - NameError, TypeError 등은 발생한 예외 타입의 종류(이름)
- 모든 내장 예외는 Exception Class를 상속받아 이뤄짐
- 사용자 정의 예외를 만들어 관리할 수 있음

![image-20220124214927705](에러,예외 처리(Error,Exception Handling).assets/image-20220124214927705.png)

![image-20220124214943447](에러,예외 처리(Error,Exception Handling).assets/image-20220124214943447.png)

![image-20220124214952567](에러,예외 처리(Error,Exception Handling).assets/image-20220124214952567.png)

![image-20220124214959437](에러,예외 처리(Error,Exception Handling).assets/image-20220124214959437.png)

![image-20220124215009794](에러,예외 처리(Error,Exception Handling).assets/image-20220124215009794.png)

![image-20220124215018416](에러,예외 처리(Error,Exception Handling).assets/image-20220124215018416.png)

![image-20220124215024719](에러,예외 처리(Error,Exception Handling).assets/image-20220124215024719.png)

![image-20220124215030942](에러,예외 처리(Error,Exception Handling).assets/image-20220124215030942.png)

![image-20220124215038268](에러,예외 처리(Error,Exception Handling).assets/image-20220124215038268.png)

![image-20220124215045079](에러,예외 처리(Error,Exception Handling).assets/image-20220124215045079.png)

![image-20220124215054357](에러,예외 처리(Error,Exception Handling).assets/image-20220124215054357.png)

![image-20220124215101544](에러,예외 처리(Error,Exception Handling).assets/image-20220124215101544.png)





> 예외처리

- try문 (statement) / except 절(clause)을 이용하여 예외 처리를 할 수 있다
- try 문
  - 오류가 발생할 가능성이 있는 코드를 실행
  - 예외가 발생되지 않으면, except 없이 실행 종료
- except 문
  - 예외가 발생하면, except 절이 실행
  - 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함



```python
try:						   # 주의사항 : try문은 반드시 한 개 이상의
    try 명령문					 # except문이 필요
except 예외그룹-1 as 변수-1:
    예외처리 명령문 1
except 예외그룹-2 as 변수-2:
    예외처리 명령문 2
finally:                       # 선택사항
    finally 명령문
```

```python
try:
    num = input('숫자입력:')
    print(int(num))
except ValueError:
    print('숫자가 입력되지 않았습니다.')
    
# 숫자입력 :3
# 숫자가 아닙니다(다른거 입력시)
```





> 예외 발생 시키기

- raise 를 통해 예외를 강제로 발생

  raise <표현식>(메시지)

![image-20220124215639401](에러,예외 처리(Error,Exception Handling).assets/image-20220124215639401.png)

- assert 를 통해 예외를 강제로 발생
- assert는 상태를 검증하는데 사용되며, 무조건 AssertionError가 발생
- 일반적으로 디버깅 용도로 사용

![image-20220124220039405](에러,예외 처리(Error,Exception Handling).assets/image-20220124220039405.png)