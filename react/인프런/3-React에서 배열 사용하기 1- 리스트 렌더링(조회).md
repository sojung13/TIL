![image-20220705103240140](3-React에서 배열 사용하기 1- 리스트 렌더링(조회).assets/image-20220705103240140.png)







![image-20220705103942352](3-React에서 배열 사용하기 1- 리스트 렌더링(조회).assets/image-20220705103942352.png)

```js
// App.js

import './App.css';
import DiaryEditor from './DiaryEditor.js'
import DiaryList from './DiaryList.js'

const dummyList = [
  {
    id : 1,
    author: '박소정',
    content : '리액트 잘하고 싶다',
    emotion: 4,
    created_date: new Date().getTime()
  },
  {
    id: 2,
    author: '박재범',
    content: '원소주 원해',
    emotion: 5,
    created_date: new Date()
  }
]

function App() {
  return (
    <div className="App">
      <DiaryEditor></DiaryEditor>
      <DiaryList dummyList={dummyList}></DiaryList>
    </div>
  );
}

export default App;
```

```js
// DiaryList.js

const DiaryList = ({dummyList}) => {
  console.log(dummyList)
  return (
    <div className="DiaryList">
      <h2>HIHI</h2>

    </div>
  )
}

export default DiaryList;
```

- `props`를 통해 App.js에서 저장된 더미 리스트를 DiaryList에 내려준다.
- 그리고 console.log를 통해 잘 전달되었는지 확인해준다!!



---

![image-20220705104714594](3-React에서 배열 사용하기 1- 리스트 렌더링(조회).assets/image-20220705104714594.png)

```js
const DiaryList = ({dummyList}) => {
  console.log(dummyList)
  return (
    <div className="DiaryList">
      <h2>HIHI</h2>
      <div>{dummyList.length}개의 일기가 있습니다.</div>
      <div>
        {dummyList.map((it)=> (
          <div>
            <div>일기 작성자 : {it.author}</div>
            <div>일기 내용 : {it.content}</div>
            <div>일기 감정 : {it.emotion}</div>
          </div>
        ))}
      </div>
    </div>
  )
}

DiaryList.defaultProps = {
  diaryList: []
}

export default DiaryList;
```

- 가장 하단의 `defaultProps`는 props가 되지 않은 경우 보여줄 초기 상태를 의미한다.
- 빈 배열로 해두어서 만약 상단 js 파일에서 어떤 데이터도 전달받지 않은 경우엔 빈 배열을 보여줄 수 있다.
- `map` 내장함수를 통해 하나하나 꺼내고 점 표기법으로 각각의 데이터에 접근이 가능하다.



----



![image-20220705112314623](3-React에서 배열 사용하기 1- 리스트 렌더링(조회).assets/image-20220705112314623.png)

- 위의 일련의 과정을 거쳐 dummyList의 요소 하나하나를 가져오면 위와 같은 에러가 뜬다.
- 말인 즉슨 각각의 아이템들은 고유 키가 필요하다는 뜻!

```js
const DiaryList = ({dummyList}) => {
  console.log(dummyList)
  return (
    <div className="DiaryList">
      <h2>HIHI</h2>
      <div>{dummyList.length}개의 일기가 있습니다.</div>
      <div>
      	// {dummyList.map((it,idx)=>
      	// 고유의 인덱스로 뽑아주는 방법도 있지만
      	// 아이템들마다 id가 있는 경우 id를 사용하는 것이 가장 좋다.
        {dummyList.map((it)=> (
          <div key={it.id}>
            <div>일기 작성자 : {it.author}</div>
            <div>일기 내용 : {it.content}</div>
            <div>일기 감정 : {it.emotion}</div>
          </div>
        ))}
      </div>
    </div>
  )
}

DiaryList.defaultProps = {
  diaryList: []
}

export default DiaryList;
```



----



![image-20220705113748845](3-React에서 배열 사용하기 1- 리스트 렌더링(조회).assets/image-20220705113748845.png)

```js
// DiaryItem.js

const DiaryItem = ({author, content, created_date, emotion, id}) => {
  return (
    <div
     className="DiaryItem">
      <div className="info">
        작성자 : {author}
        감정 점수 : {emotion}
        일기 : {content}
        <br></br>
        <span className="date">
          {new Date(created_date).toLocaleString()}
        </span>
      </div>
      <div className="content">{content}</div>
     </div>
  )
}

export default DiaryItem;
```

```js
// DiaryList.js

      <div>
        {dummyList.map((it)=> (
          <DiaryItem key={it.id} {...it}>
          </DiaryItem>
        ))}
      </div>
```

- DiaryList.js에서 props로 DiaryItem에 정보를 넘겨준다.
- 이때 위와 동일하게 key 값으로 id를 주고, spread 연산자를 통해 전부 넘겨준다.
- 각각의 정보를 넘겨받은 DiaryItem에서는 하나하나 꺼내 작성하면 된다.