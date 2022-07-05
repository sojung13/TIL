```js
// App.js

import './App.css';
import DiaryEditor from './DiaryEditor.js'
import DiaryList from './DiaryList.js'
import { useRef, useState } from 'react'

function App() {
  const [data, setData] = useState([])

  const dataId = useRef(0)

  const onCreate = (author,content,emotion) => {
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
  }

  const onRemove = (targetId) => {
    console.log(`${targetId}가 삭제되었습니다`)
    const newDiaryList = data.filter((it)=> it.id !== targetId)
    setData(newDiaryList)
  }

  return (
    <div className="App">
      <DiaryEditor onCreate={onCreate}></DiaryEditor>
      <DiaryList diaryList={data}
        onRemove={onRemove}
      ></DiaryList>
    </div>
  );
}

export default App;
```

```js
// DiaryList.js

import DiaryItem from "./DiaryItem"

const DiaryList = ({diaryList, onRemove}) => {
  console.log(diaryList)
  return (
    <div className="DiaryList">
      <h2>HIHI</h2>
      <div>{diaryList.length}개의 일기가 있습니다.</div>
      <div>
        {diaryList.map((it)=> (
          <DiaryItem key={it.id} {...it} onRemove={onRemove}>
          </DiaryItem>
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

```js
// DiaryItem.js

const DiaryItem = ({author, content, created_date, emotion, id, onDelete}) => {
  return (
    <div
     className="DiaryItem">
      <div className="info">
        작성자 : {author} | 
        감정 점수 : {emotion} | 
        <br></br>
        <span className="date">
          {new Date(created_date).toLocaleString()}
        </span>
      </div>
      <div className="content">{content}</div>
      <button onClick={()=> {
        // 여기서 onClick 함수 안의 코드가 너무 길다고 생각이 들면
        // 이 부분을 바깥으로 빼는 방법도 있다!!!!!
        if(window.confirm(`${id}번째 일기를 삭제할 겁니까?`)) {
          onDelete(id)
        }
      }}>삭제하기</button>
     </div>
  )
}

export default DiaryItem;
```

```js
// DiaryItem.js 수정 ver

const DiaryItem = ({author, content, created_date, emotion, id, onRemove}) => {

  // 여기다가 새로운 함수를 작성하고 난 뒤 onClick 안에 함수명을 작성해주면 된다.
  const handleRemove = () => {
    if(window.confirm(`${id}번째 일기를 삭제할 겁니까?`)) {
      onRemove(id)
    }
  }

  return (
    <div
     className="DiaryItem">
      <div className="info">
        작성자 : {author} | 
        감정 점수 : {emotion} | 
        <br></br>
        <span className="date">
          {new Date(created_date).toLocaleString()}
        </span>
      </div>
      <div className="content">{content}</div>
      <button onClick={handleRemove}>삭제하기</button>
     </div>
  )
}

export default DiaryItem;
```



