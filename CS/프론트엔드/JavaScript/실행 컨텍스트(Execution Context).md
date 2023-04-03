### 실행 컨텍스트 (Execution Context)

✅ **코드의 실행환경에 대한 여러가지 정보를 담고 있는 개념** 으로, 간단히 말하자면 자바스크립트 엔진에 의해 만들어지고 사용되는 코드 정보를 담은 객체의 집합이라고 할 수 있다.

![image-20230331192559661](../../../../../../AppData/Roaming/Typora/typora-user-images/image-20230331192559661.png)

```javascript
var global = 'global';

function foo() {
    var local1 = 'local1';

    function bar() {
        var local2 = 'local2';
        console.log(local1, local2, global); //local1 local2 global
    }

    bar();
}

foo();
```



#### 실행 컨텍스트 스택 (Execution Context Stack)

실행 컨텍스트가 생성되면 흔히 콜 스택(Call Stack)이라고도 불리는 실행 컨텍스트 스택에 쌓이게 된다. **GEC(글로벌 실행 컨텍스트, Global Execution Context)**는 코드를 실행하기 전에 쌓이고 모든 코드를 실행하면 제거된다. **FEC (함수 실행 컨텍스트, Function Execution Context)**는 호출할 때 쌓이고 호출이 끝나면 제거된다.

```javascript
function func() {
  console.log('함수 실행 컨텍스트');
}
console.log('글로벌 실행 컨텍스트');
func();
```

제일 처음, 코드를 실행하기 전에 GEC가 쌓이고 코드를 실행하면서 콘솔에 "글로벌 실행 컨텍스트"가 출력된다. 그 다음 func()을 호출하고 그에 대한 FEC가 만들어져 쌓이고 FEC를 실행하며 콘솔에 "함수 실행 컨텍스트"가 출력된다. 이후 func()이 종료되고 FEC가 스택에서 제거된 후, 모든 코드의 실행이 끝나면서 GEC가 스택에서 제거된다.



#### 구성 요소

실행 컨텍스트는 다음과 같은 구성 요소를 갖는다.

- Lexical Environment
- Variable Environment
- this 바인딩



**Lexical Environment** : 변수 및 함수 등의 식별자(Identifier) 및 외부 참조에 관한 정보를 가지고 있는 컴포넌트. Environment Record와 outer, 이 두 가지 구성 요소를 갖는다.

```javascript
var x = 10;
 
function foo() {
  var y = 20;
  console.log(x);
}
```

```javascript
// 위 코드에 대해 이러한 렉시컬 환경이 형성된다.

globalEnvironment = {
	environmentRecord = { x: 10 },
	outer: null
}
fooEnvironment = {
	environmentRecord = { y: 20 },
	outer: globalEnvironment
}
```

> 따라서 foo()에서 x를 참조할 때는 현대 Environment Record를 찾아보고 없기 때문에 outer 참조를 사용하여 외부의 Lexical Environment에 속해 있는 Enviroment Record를 찾아보는 방식이다.



**Variable Environment** : Lexical Environment와 동일한 성격을 가지지만 `var`로 선언된 변수만 저장한다는 점에서 다르다. 즉, Lexical Environment는 `var`로 선언된 변수를 제외하고 나머지(`let`으로 선언되었거나 함수 선언문)를 저장한다.



**this 바인딩**

this의 바인딩은 실행 컨텍스트가 생성될 때마다 this 객체에 어떻게 바인딩이 되는지를 나타낸 것이다. (ES6부터 this의 바인딩이 LexicalEnvironment 안에 있는 EnvironmentRecord 안에서 일어난다는 사실을 기억해두도록 하자. 그렇게 중요하진 않으니 알고만 있자.)

- ***GEC의 경우***
  - strict mode라면 `undefined` 로 바인딩된다.
  - 아니라면 글로벌 객체로 바인딩된다. (브라우저에선 window, 노드에선 global)
- ***FEC의 경우***
  - 해당 함수가 어떻게 호출되었는지에 따라 바인딩된다.



#### 과정

EC는 2 가지 과정을 거친다.

1. Creation Phase(생성 단계)
2. Execution Phase(실행 단계)

**생성단계** : 생성 단계는 다시 3 가지 단계로 이루어진다.

1. Lexical Environment 생성
2. Variable Environment 생성
3. this 바인딩

