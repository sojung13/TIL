```js
const memoizedCallback = useCallback(
	() => {
        doSomething(a,b);
    },
    [a,b]
)
```

> useCallback

- 메모이제이션된 콜백을 반환
- 첫번째 인자로 넘어온 함수, 두번째 인자로 넘어온 배열 내의 값이 변경될 때까지 저장해놓고 재사용할 수 있도록 해준다.
- 해당 컴포넌트가 랜더링되더라도 그 함수가 의존하는 값들이 바뀌지 않는 한 기존 함수를 계속해서 반환한다. 즉 a와 b의 값이 동일하다면 다음 랜더링때 이 함수를 재사용하고, a 또는 b의 값이 바뀌면 새로운 함수가 생성되어 memoizedCallback 변수에 할당된다.



----



```js
  const onCreate = useCallback(
    (author,content,emotion) => {
      const created_date = new Date().getTime();
      const newItem = {
        author,
        content,
        emotion,
        created_date,
        id : dataId.current
      }
    dataId.current += 1
    setData([newItem, ...data])
  },
  [data])
```

