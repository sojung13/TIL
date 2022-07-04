### 2-1 Truthy & Falsy

TRUE : "string"(비어있지 않은 문자열), {}, 숫자형, Infinity, 

False : ""(빈 문자열), undefined, null, 0, -0, NaN, 



---



### 2-2 삼항 연산자

```js
let a = 3
a > 0? console.log('양수입니다') : console.log('음수입니다')
```

- if문을 지우고 if 문에 해당하는 절을 `?` 왼쪽에, 그리고 : 좌 우로 조건에 맞는 참 거짓을 작성해주면 된다.

```js
let score = 80;

score >= 90 ? console.log('A입니다')
	: score >= 50
	? console.log('B 입니다')
	: console.log('낙제입니다')
```

- 위와 같이 중첩으로 삼항 연산자를 사용할 수 있으나 보기 불편하기 때문에 if문으로 바꿔버리는 것이 더 편하다.



----



### 2-3 단락 회로 평가

```js
console.log(true && true)		// and을 뜻함
console.log(true || false)		// or을 뜻함
console.log(!true)				// not을 뜻함
```

`단락 회로 평가`는 왼쪽에서 오른쪽으로 연산하게 되는 논리연산자의 연산 순서를 이용하는 문법을 의미한다.

```js
// && 연산자
console.log(false && true)		// false

// && 연산자는 피연산자 2개가 모두 true일 때만 true를 반환한다.
// 첫 번째 연산자가 false이면 두 번째 연산자는 굳이 볼 필요가 없어진다.
```

```js
// || 연산자
console.log(false || true)		// true

// || 연산자는 둘 중 하나만 true여도 true이다.
// 앞 뒤 상관 없이 어떤 연산자가 true든 true를 보기만 하면 종료가 된다.
```

```js
const getName = (person) => {
    return person && person.name	// && 연산자로, person이 이미 falsy한 속성을 가지고 있음
}

let person;							// undefined로 설정된 경우임

const name = getName(person)
console.log(name)					// undefined
```

```js
const getName = (person) => {
    const name =  person && person.name		// person이 이미 null로, falsy한 값을 가짐
	return name || '객체가 아닙니다'			// 고로 '객체가 아닙니다'가 출력되는 구조
}

let person = null;

const name = getName(person)
console.log(name)							// '객체가 아닙니다'
```

```js
const getName = (person) => {
    const name= person && person.name		// person이 '소정'을 가지기 때문에 truthy함
    return name || '객체가 아닙니다'			// 고로 그대로 name을 출력
}

let person = { name : '소정'};

const name = getName(person)
console.log(name)							// '소정'
```



-----



### 2-4 조건문 업그레이드

```js
function isKoreanFood(food) {
    if(food === '불고기' || food === '비빔밥' || food === '떡볶이') {
        return true
    }
    return false
}

const food1 = isKoreanFood('불고기')
const food2 = isKoreanFood('파스타')

console.log(food1)
console.log(food2)
```

- 위와 같이 작성하면 코드 길이가 너무 길어진다. 
- switch문으로 바꿔도 매한가지! 그래서 새로운 조건문의 중요성이 등장한다.

```js
function isKoreanFood(food) {
    if (['불고기','떡볶이','비빔밥'].includes(food)) {
        return true
    }
    return false
}

const food1 = isKoreanFood('불고기')
const food2 = isKoreanFood('파스타')

console.log(food1)
console.log(food2)
```

- 👉 존재하는지 존재하지 않는지 true || false로 알아보기

```js
const getMeal = (mealType) => {
    if(mealType === '한식') return '불고기';
    if(mealType === '양식') return '파스타';
    if(mealType === '일식') return '초밥';
    if(mealType === '중식') return '짜장면';
    return '굶기'
}

console.log(getMeal('한식'))
```

- 👉 주어진 값에 따라 각각 다른 결과를 반환하는 함수.
- 만약 이보다 더 긴 사례들을 다 적어줘야 한다면 코드길이가 무한대로 길어질 것이다.

```js
const meal = {
  한식: "불고기",
  중식: "멘보샤",
  양식: "파스타",
  일식: "초밥"
};

const getMeal = (mealType) => {
  return meal[mealType] || "굶기";
};

console.log(getMeal("한식"));
```

- 그럴때, 객체의 프로퍼티에 접근하는 `괄호표기법`을 사용하여 코드를 더 효율적으로 작성할 수 있다.