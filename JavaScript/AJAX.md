## AJAX

> AJAX란

- Asynchronous JavaScript And XML(비동기식 JavaScript와 XML)
- 서버와 통신하기 위해 `XMLHttpRequest` 객체 활용
- JSON, XML, HTML 그리고 일반 텍스트 형식 등을 포함한 다양한 포맷을 주고받을 수 있음
- 페이지 전체를 reload(새로 고침)를 하지 않고서도 수행되는 `비동기성`
  - 서버의 응답에 따라 전체 페이지가 아닌 일부분만을 업데이트할 수 있음
- AJAX의 주요 두가지 특징은 아래의 작업을 할 수 있게 해줌
  - 페이지 새로 고침 없이 서버에 요청
  - 서버로부터 데이터를 받고 작업을 수행



> XMLHttpRequest 객체

- 서버와 상호작용하기 위해 사용되며 전체 페이지의 새로 고침 없이 데이터를 받아올 수 있음
- 사용자의 작업을 방해하지 않으면서 페이지 일부를 업데이트할 수 있음
- 주로 AJAX 프로그래밍에 사용
- 이름과 달리 XML뿐만 아니라 모든 종류의 데이터를 받아올 수 있음
- 생성자 = XMLHttpRequest()



> XMLHttpRequest 예시

```js
const request = new XMLHttpRequest()
const URL = 'https://jsonplaceholder.typecode.com/todos/1/'

request.open('GET',URL)
request.send()

const todo = request.response
console.log(`data: ${todo}`)
```

- console에 todo 데이터가 출력되지 않음
- 데이터 응답을 기다리지 않고 console.log()를 먼저 실행했기 때문





----





## Asynchronous JavaScript

> 동기식

- 순차적, 직렬식 Task 수행
- 요청을 보낸 후 응답을 받아야만 다음 동작이 이루어짐(blocking)



> 비동기식

- 병렬적 Task 수행
- 요청을 보낸 후 응답을 기다리지 않고 다음 동작이 이루어짐(non-blocking)
- 요청을 보내고 응답을 기다리지 않고 다음 코드가 실행됨



> 왜 비동기(Asynchronous)를 사용하는가?

- "사용자 경험"
  - 매우 큰 데이터를 동반하는 앱이 있다고 가정
  - `동기식 코드라면` 데이터를 모두 불러온 뒤 앱이 실행됨
    - 즉, 데이터를 모두 불러올 때 까지는 앱이 모두 멈춘 것으로 보임
    - 코드 실행을 차단하여 화면이 멈추고 응답하지 않는 것 같은 사용자 경험을 제공
  - ✅ `비동기식 코드라면` 데이터를 요청하고 응답 받는 동안, 앱 실행을 함께 진행함
    - 데이터를 불러오는 동안 지속적으로 응답하는 화면을 보여줌으로써 더욱 쾌적한 사용자 경험을 제공
  - 때문에 많은 웹 API 기능은 현재 비동기 코드를 사용하여 실행됨 



> "JavaScript는 single threaded이다"

- 컴퓨터가 여러 개의 CPU를 가지고 있어도 main thread라 불리는 단일 스레드에서만 작업 수행
- 즉, 이벤트를 처리하는 `Call Stack`이 하나인 언어라는 의미
- 이 문제를 해결하기 위해 JavaScript는
  - 즉시 처리하지 못하는 이벤트들을 다른 곳

