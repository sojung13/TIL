## Vue

> 왜 Vue를 사용할까?

- 현대 웹 페이지는 페이지 규모가 계속해서 커지고 있으며, 그만큼 사용하는 데이터도 늘어나고 사용자의 상호작용도 많이 이루어짐
- 결국 Vanilla JS만으로는 관리하기가 어려움



> 비교

##### ❤️ Vanilla JS

- 한 유저가 작성한 게리글이 DOM 상에 100개 존재
- 이 유저가 닉네임을 변경하면, DB의 Update와 별도로 DOM 상의 100개의 작성자 이름이 모두 수정되어야 함
- '모든 요소'를 선택해서 '이벤트'를 등록하고 값을 변경해야 함



##### ✔️💙Vue.js

- DOM과 Data가 연결되어 있고
- Data를 변경하면 이에 연결된 DOM은 알아서 변경
- 즉, 우리가 신경 써야 할 것은 오직 `Data에 대한 관리`



-----



### Concepts of Vue.js

> MVVM Pattern

- 애플리케이션 로직을 UI로부터 분리하기 위해 설계된 디자인 패턴
- 구성 요소 
  - Model
    - "Vue에서 Model은 JavaScript Object다."
    - Object === { key:value }
    - Model은 Vue Instance 내부에서 Data라는 이름으로 존재
    - 이 data가 바뀌면 View(DOM)가 반응
  - View
    - "Vue에서 View는 DOM(HTML)이다"
    - Data의 변화에 따라서 바뀌는 대상
  - View Model
    - "Vue에서 ViewModel은 모든 Vue Instance이다."
    - View와 Model 사이에서 Data와 DOM에 관련된 모든 일을 처리
    - ViewModel을 활용해 Data를 얼마만큼 잘 처리해서 보여줄 것인지(DOM)를 고민하는 것



----



### Quick Start of Vue.js

> 공식문서 시작하는 방법

1. CDN 작성

```html
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```

2. 선언적 렌더링

```html
<h2>선언적 렌더링</h2>
<div id="app">
    {{ message }}
</div>


var app = new Vue({
	el: '#app',
	data : {
		message: '안녕하세요 Vue!'
	}
})
```

3. Element 속성 바인딩

```html
<h2>Element 속성 바인딩</h2>
<div id="app-2">
    <span v-bind:title="message">
        내 위에 잠시 마우스를 올리면 동적으로 바인딩 된 title을 볼 수 있습니다!
    </span>
</div>

var app2 = new Vue({
	el: '#app-2',
	data: {
		message: '이 페이지는' + new Date() + '에 로드 되었습니다'
	}
})
```

4. 조건문

```html
<h2>조건</h2>
<div id="app-3">
    <p v-if="seen">
        이제 나를 볼 수 있어요
    </p>
</div>

var app3 = new Vue({
	el: '#app-3',
	data: {
		seen: true  // false로 토글 가능
	}
})
```

5. 반복문

```html
<h2>반복</h2>
<div id="app-4">
    <ol>
        <li v-for="todo in todos">
            {{ todo.text }}
        </li>
    </ol>
</div>

var app4 = new Vue({
	el: '#app-4',
	data: {
		todos: [
			{text : "JavaScript 배우기"},
			{text : "Vue 배우기"},
			{text : "행복하자"},
		]
	}
})
```

