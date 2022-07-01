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

    console.log(`${currentKey} : ${currentValye}`);
}

// value만 뽑고 싶다면 key를 뽑을 필요가 없다.

const personValues = Obkects.values(person);

for (let i=0; )
```

