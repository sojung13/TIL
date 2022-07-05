### 1-5 함수

```js
let width1 = 10;
let height1 = 20;
let area1 = width1 * height1
console.log(area1)					// 200

let width2 = 30;
let height2 = 10;
let area2 = width2 * height2
console.log(area2)					// 300

// 위와 같이 중복된 코드를 계속 작성하는 것이 번거로우니 할 수 있는 것이 바로 함수작성이다!!!

const getArea = (width, height) => {
    let area = width * height
    console.log(area)
}	// 함수 선언식, 함수 선언 방식의 함수 생성

getArea(10,20)						// 200
```



------



### 1-6 함수 표현식 & 화살표 함수

```js
let hello = function () {
    return '안녕하세요 여러분'
}	// 함수 표현식

console.log(hello)					// f hello() (함수를 담고 있다는 뜻)

const helloText = hello()
console.log(helloText)				// 안녕하세요 여러분

// 화살표 함수

let helloA = () => {
    return '안녕하세요 여러분'
}
```

> 함수 선언식과 함수 표현식의 차이점

- 함수 선언삭 : 함수를 바로 선언. 함수 호이스팅 가능

- 함수 표현식 : 변수 안에서 함수를 선언. 함수 호이스팅 불가능

- ```js
  console.log(helloB())			// 안녕하세요 여러분
  console.log(helloA())			// error
  
  let helloA = function() {
      return '안녕하세요 여러분'
  } // 함수 표현식
  
  function helloB() {
      return '안녕하세요 여러분'
  } // 함수 선언식
  ```

  

------



### 1-7 콜백 함수

```js
function checkMood (mood, goodCallback, badCallback) {
    if(mood === 'good') {
        // 기분 좋을 때 하는 동작
        goodCallback();
    } else {
        // 기분 안 좋을 때 하는 동작
        badCallback();
    }
}

function cry() {
    console.log('ACTION : CRY')
}

function sing() {
    console.log('ACTION : SING')
}

function dance() {
    console.log('ACTION : DANCE')
}

checkMood('good',sing,cry)				// ACTION : SING
```

- 콜백함수 = 함수의 파라미터 안에 함수를 넘겨주는 것



----



### 1-8 객체

```js
// 객체 프로퍼티 선언하는 방법

let person = new Object();
let person2 = {
    key : 'value',		// 프로퍼티 (객체 프로퍼티)
    key2 : 'value2',
    key3 : true,
    key4 : undefined,
    key5 : [1,2,3],
    key6 : function() {}
};						// 객체 리터럴 방식. 주로 이 방식으로 작성한다.

console.log(person2);
console.log(person2.key2);		// 점 표기법. value2
console.log(person2['key4']);		// 괄호 표기법. 무조건 문자열로 해주어야 한다.

function getPropertyValue(key) {
    return person2[key];
}

console.log(getPropertyValue('key3'))	// true
```

```js
// 객체 프로퍼티 추가, 수정, 삭제하는 방법

let person = {
    name : '박소정',
    age : 27
}

person['gender'] = 'woman'
person.location = '한국'					// 점 표기법이나 괄호 표기법으로 프로퍼티 추가 가능
console.log(person['location'])			// '한국'

person.name = 'sojungPark'
console.log(person.name)				// sojungPark. 수정도 가능

delete person['name']					// 삭제도 가능
// 하지만 delete를 사용해도 메모리를 사용하기 때문에 아래와 같이 null로 변환하는 것을 추천한다.
person.name = null

// let person뿐만 아니라 const으로 지정된 프로퍼티도 수정이 가능하다!
// 상수여도 person 자체를 수정하는 것이 아니라 프로퍼티'만' 바꾸는 행위이기 때문
// 대신 아래와 같이 person 자체를 건드리려고 하는 것은 const로는 안된다.

person = {
    // 위에서 이미 person이 선언이 됨
}
```

```js
// 객체 프로퍼티 안에 함수가 들어가는 것도 가능. 이를 '메서드'라고 부른다.

const person = {
    name : '박소정',					// 멤버(함수가 아닌 다른 객체들을 지칭)
    age : 25,						  // 멤버
    say : function() {
        console.log('안녕안녕')			// 메서드
    },
    say2 : function() {
        console.log(`안녕 ${this.name}`);
        console.log(`안녕 ${this['name']}`);
        console.log(`안녕 ${person.name}`);
        console.log(`안녕 ${person['name']}`);
    }
}

person.say()							// 안녕안녕
person['say']()							// 안녕안녕

person.say2()							// 안녕 박소정
person['say2']()						// 안녕 박소정
```

```js
// in 연산자
// 프로퍼티의 존재 여부를 boolean 형태로 전달받을 수 있다.
// 객체에서 무조건 key 값을 찾을 때만 사용된다!!!! value값 찾기 불가능

const person = {
    name : '박소정',
    age : 27
}

console.log(${'name' in person})		// true
console.log(${'gender' in person})      // false
console.log('name' in person)			// true
```



