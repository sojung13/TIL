### 2-9 async & await - 직관적인 비 동기 처리 코드 작성하기

```js
function hello() {
    return 'hello'
}

async function helloAsync() {
    return 'hello Async'
}

console.log(hello())			// hello
console.log(helloAsync())		// Promise{<pending>}
```

- 만일 마우스 커서를 갖다댔을 때, Promise 객체가 뜬다는 것은 `then`을 사용해도 된다는 뜻이 되기도 한다.



```js
function hello() {
  return "hello";
}

async function helloAsync() {
  return "hello async";
}

helloAsync().then((res) => {
  console.log(res);				// hello async
});
```

- `async`를 붙이면 promise가 되면서 자동으로 return 안에 있는 값은 `resolve` 값이 된다.
- 즉, `async`는 Promise가 되도록 해준다.



```js
function delay(ms) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve();
    }, ms);
  });
}

async function helloAsync() {
  await delay(3000);
  return "hello async";
}

helloAsync().then((res) => {
  console.log(res);
});
```

- `await`을 비동기 함수 앞에 붙이면 비동기 함수가 마치 동기 함수가 된 것처럼 작동하게 된다.
- 말인 즉슨, `await` 함수가 붙은 함수는 그 줄의 함수가 다 수행될 때까지 밑에 작성된 함수들은 일절 작동하지 않게 된다.



```js
function delay(ms) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve();
    }, ms);
  });
}

async function helloAsync() {
  await delay(3000);
  return "hello async";
}

async function main() {
  const res = await helloAsync();
  console.log(res);
}

main();
```

- `await`과 `async`를 사용하면 비동기 함수를 마치 동기 함수를 작동시킨 것처럼 사용할 수 있게 된다.



> await과 async

- `await` : Promise 객체를 입히는 것
- `async` : Promise 객체를 해독/ 해제하는 것
