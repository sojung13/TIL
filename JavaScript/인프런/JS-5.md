### 2-5 비 구조화 할당

> 배열에서의 비 구조화 할당

```js
let arr = ['one','two'.'three']

let one = arr[0]
let two = arr[1]
let three = arr[2]

console.log(one,two,three)
```

- 이렇게 작성하기보다, 



```js
let arr = ['one','two'.'three']

let [one, two, three] = arr

console.log(one,two,three)
```

- 이렇게 `비 구조화 할당(구조 분해 할당)`을 사용하면 원하는 값을 더 쉽고 빠르게 사용할 수 있다.



```js
let [one,two,three] = ['one','two','three']
console.log(one,two,three)
```

- 위와 같이 더 축약해서 작성 가능!! `배열의 선언 분리 / 비 구조화 할당`이라고 한다.



```js
let [one,two,three,four='four'] = ['one','two','three']
console.log(one,two,three)
```

- 앞에서부터 차례대로 배열이 선언되는 가운데, 위와 같이 선언할 때 같이 값도 작성해주는 방법이 있다.
- 만일 값을 입력하지 않으면 `undefined`로 입력된다.



```js
let a = 10;
let b = 20;

[a,b] = [b,a]
console.log(a,b)				// 20 10
```

- 비 구조화 할당을 통해 값이 스왑되는 모습을 확인할 수 있다.



----



> 객체에서의 비 구조화 할당

```js
let object = { one : 'one', two : 'two', three : 'three'}

let one = object.one
let two = object.two
let three = object.three

console.log(one, two, three)
```

- 객체의 이 반복적인 부분을 비구조화 할당을 통해 짧은 출력 역시 가능하다.



```js
let object = { one : 'one', two : 'two', three : 'three'}

let { one, two, three } = object

console.log(one, two, three)		// one two three
```

- 순서가 아니라 키 값을 기준으로 값이 할당된다.

- ```js
  let object = { one : 'one', two : 'two', three : 'three'}
  
  let { one, two, sojung } = object
  
  console.log(one, two, sojung)		// one two undefined
  ```

- 만약 변수의 이름을 바꾸고 싶다면 아래와 같이 작성하면 된다.

- ```js
  let object = { one : 'one', two : 'two', three : 'three'}
  
  let { one, two, three : sojung } = object
  // three의 값을 sojung이라는 변수명에 할당하겠다는 의미다.
  
  console.log(one, two, sojung)		// one two three
  ```

  



-----



### 2-6 Spread 연산자

```js
const cookie = {
    base : 'cookie',
    madeIn : 'korea'
}

const chocoCookie = {
    base : 'cookie',
    madeIn : 'korea',
    toping : 'choco'
}

const cheeseCookie = {
    base : 'cookie',
    madeIn : 'korea',
    toping : 'cheese'
}

const strawberryCookie = {
    base : 'cookie',
    madeIn : 'korea',
    toping : 'strawberry'
}
```

- 이렇게 연달아 작성하면 중복되는 코드도 있고 너무 길어진다!!!!!! 



```js
const cookie = {
    base : 'cookie',
    madeIn : 'korea'
}

const chocoCookie = {
	... cookie,
    toping : 'choco'
}

const cheeseCookie = {
	... cookie,
    toping : 'cheese'
}

const strawberryCookie = {
	... cookie,
    toping : 'strawberry'
}
```

- 이렇게 겹치는 코드는 `Spread연산자`를 활용하여 코드를 축약할 수 있다.



```js
const noTopingCookies = ['촉촉한 쿠키','안 촉촉한 쿠키']
const topingCookies = ['바나나쿠키','블루베리쿠키','딸기쿠키','초코칩쿠키']

const allCookies= [...noTopingCookies, '함정쿠키',...topingCookies]
```

- `concat` 내장함수를 사용해서 새로운 배열을 만드는 것도 가능하지만, 이렇게 `spread 연산자`를 사용하면 중간에 값을 추가하는 등 더욱 유연하게 새로운 배열을 만들어낼 수 있다.