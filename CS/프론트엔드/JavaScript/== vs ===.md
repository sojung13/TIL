### == vs ===

💡먼저, `원시 타입`과 `참조 타입`이란!

- 원시타입 (Primitive Type)

![image-20230403195116183](../../../../../../AppData/Roaming/Typora/typora-user-images/image-20230403195116183.png)

- 참조 타입 (Reference Type)
  - 원시 타입을 제외한 타입들(문자열, 배열, 열거, 클래스, 인터페이스)

---



둘 다 동일한 비교를 하지만 엄격한 동등 비교 연산자(===)의 경우, 타입 변환(Type conversion)이 일어나지 않으며 타입이 일치해야 한다.

```javascript
'' == '0'           // false
0 == ''             // true
0 == '0'            // true

false == 'false'    // false
false == '0'        // true

false == undefined  // false
false == null       // false
null == undefined   // true

' \t\r\n ' == 0     // true
```

위 경우를 보면, 동등 비교 연산자(===)를 사용해서 여러가지 원시타입을 비교해 보았는데, 타입 변환이 발생함을 볼 수 있다.

단, 객체/배열의 경우는 참조타입이기 때문에 두 연산자 모두 동일하게 동작한다.

```javascript
var a = {}
var b = {}

a == b // false
a === b // false

var c = [];
var d = [];

c == d // false
c === d // false
```

문자열의 경우는 좀 특별한데, 자바스크립트에서 문자열은 원시타입이지만 객체로도 만들 수 있기 때문에 그 동등 비교가 다르다.

```javascript
var a = "string"
var b = new String("string")
a == b // true
a === b // false
```

퍼포먼스 측면에서는 아주 미묘한 차이가 있기 때문에 신경쓸 바가 못되고, 안전한 타입 체크와 더 좋은 코드를 위해 엄격한 동등 비교 연산자(===)를 사용하는 것이 바람직하다.