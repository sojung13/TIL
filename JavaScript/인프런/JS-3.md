### 1-9 배열

```js
let arr = new Array();

let arr2 = [];					// 배열 리터럴
console.log(arr2)				// []

let arr3 = [1,2,3,4]

let arr4 = [1,'문자',true, null, {}, [], function() {}] // 다 들어간다!!!
```

```js
let arr = [1,2,3,4,5]
console.log(arr[1])				// 인덱스로 접근 가능. 2

arr.push(6)
console.log(arr)				// [1,2,3,4,5,6]

arr.push({key:'value'})
console.log(arr)				// [1,2,3,4,5,6,Object]

console.log(arr.length)			// 7
```



----



### 1-10 반복문

```js
for (let i = 1; i <= 100; i++) {
    // 반복 수행할 명령
    console.log('박소정')
}								// 박소정 * 100
```

```js
const arr = ['a','b','c']

for (let i = 1; i <= 100; i ++) {
    console.log(arr[i])
}								// 'a','b','c'

const person = {
    name : '박소정',
    age : 27,
    height : 164
}

const personKeys = Objects.keys(person);

for (let i = 0; i < personKeys.length; i++) {
    const currentKey = personKeys[i]
    const currentValue = person[currentKey]

    console.log(`${currentKey} : ${currentValue}`);
}

// value만 뽑고 싶다면 key를 뽑을 필요가 없다.

const personValues = Objects.values(person);

for (let i=0; i < personValues.length; i++) {
    console.log(personValues[i])
}
```



----



### 1-11 배열내장함수

```js
// 1. forEach 내장함수
// 배열 안 각각의 값을 순환함

const arr = [1,2,3,4]
arr.forEach(function(elm) {
    console.log(elm)			// 1 2 3 4
    console.log(elm * 2)		// 2 4 6 8
})		
```

```js
// 2. map 내장함수
// 새로운 배열을 반환

const arr = [1,2,3,4]
const newArr = arr.map((elm) => {
    return elm * 2;
})								// 2 4 6 8
```

```js
// 3. includes 내장함수
// 주어진 배열 안에 해당 값이 존재하는지 안존재하는지 알려줌

const arr = [1,2,3,4]
let number = 3;
console.log(arr.includes(number))  // true
```

```js
// 4. indexOf 내장함수
// 존재하는지, 그리고 몇 번째 인덱스인지 알려줌
// 존재하지 않으면 -1을 반환

const arr = [1,2,3,4]
let numbet2= -3;
console.log(arr.indexOf(number))    // -1
```

```js
// 5. findIndex 내장함수
// 배열을 순회하며 조건에 맞는 가장 첫 번째 인덱스를 알려줌

const arr = [
    { color : 'red' },
    { color : 'blue' },
    { color : 'green' }
]

console.log(arr.findIndex((elm)=> {
    return elm.color === 'blue'
}))		
```

```js
// 6. find 내장함수

const arr = [
    { color : 'red' },
    { color : 'blue' },
    { color : 'green' }
]

const element = arr.find((elm)=> {
    return elm.color === 'blue'
})										// color : 'blue'
```

```js
// 7. filter 내장함수
// 필터링을 하고 싶다, 배열에 알맞는 조건의 프로퍼티만 뽑고 싶다.

const arr = [
    { num : 1, color : 'red' },
    { num : 2,  color : 'blue' },
    { num : 3,  color : 'green' }
]

console.log(arr.filter((elm)=> elm.color === 'blue'))
```

```js
// 8. slice 내장함수
// 두 개의 숫자 인자를 전달받음. 안넣으면 배열 그대로가 출력된다.
// a부터 b까지의 인덱스 안의 요소들만 반환해준다.

const arr = [
    { num : 1, color : 'red' },
    { num : 2,  color : 'blue' },
    { num : 3,  color : 'green' }
]

console.log(arr.slice(0,2));		// 첫번째 두번째 값만 나옴
```

```js
// 9. concat 내장함수
// 배열을 합쳐준다.

const arr1 = [
    { num : 1, color : 'red' },
    { num : 2,  color : 'blue' },
    { num : 3,  color : 'green' }
]

const arr2 = [
    { num : 1, color : 'red' },
    { num : 2,  color : 'blue' },
    { num : 3,  color : 'green' }
]

console.log(arr1.concat(arr2));		// arr1과 arr2를 합친 새로운 배열 반환
```

```js
// 10. sort 내장함수
// 원본 배열을 그대로 정렬해준다.
// 문자열은 그대로 정렬해주고 숫자형은 특별한 연산을 한 번 더 해주어야 한다.

let chars = ['나','가','다','사']

chars.sort()
console.log(chars)			// 가 나 다 사

let numbers = [1,2,3,10,30,20]

numbers.sort()
console.log(numbers)		// 1,10,2,20,3,30

const compare = (a,b) => {
   // 1. 같다
   // 2. 크다
   // 3. 작다
    
   if (a > b) {
       // 크다
       return 1;
   }
    
   if (a < b) {
       // 작다
       return -1;
   }
   
    // 같다
    return 0;
}

numbers.sort(compare)
console.log(numbers)			// 1,2,3,10,20,30
```

```js
// 11. join 내장함수

const arr = ['박소정','님','안녕하세요','파이팅입니다']

console.log(arr.join())			// 박소정,님,안녕하세요,파이팅입니다
console.log(arr.join(""))		// 박소정 님 안녕하세요 파이팅입니다
console.log(arr.join(*))		// 박소정*님*안녕하세요*파이팅입니다
```

