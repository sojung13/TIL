템플릿 리터럴

![image-20220620094354574](JavaScript.assets/image-20220620094354574.png)



함수 표현식은 호이스팅이 일어나지 않고, 함수 선언식만 호이스팅이 일어난다!

![image-20220620113206505](JavaScript.assets/image-20220620113206505.png)



콜백 함수 : 함수의 파라미터로 함수를 넘기는 것

![image-20220620120006616](JavaScript.assets/image-20220620120006616.png)



![image-20220620140136367](JavaScript.assets/image-20220620140136367.png)

점 표기법 / 괄호 표기법으로 property 추가 가능



![image-20220620142739267](JavaScript.assets/image-20220620142739267.png)

1. 초기식 `let i = 1;` : 반복의 주체가 될 변수를 우리가 선언하게 해준다!
2. 조건 : 반복이 이 조건을 만족할 때만 돌아가게 해라!
3. 연산 : 반복이 한 번 수행될 때마다 해줄 연산!



![image-20220621001902593](JavaScript.assets/image-20220621001902593.png)

- forEach : 배열의 하나하나를 호출

![image-20220621002440034](JavaScript.assets/image-20220621002440034.png)

- map: 배열 하나하나 호출. 어떤 연산 작업을 통해 나온 결과값만을 리턴한다.

![image-20220621002750629](JavaScript.assets/image-20220621002750629.png)

- includes : === 연산을 통해서 값을 찾는 함수

![image-20220621003355396](JavaScript.assets/image-20220621003355396.png)

- findIndex : 인덱스 반환. 없는 경우 -1 반환

![image-20220621010859363](JavaScript.assets/image-20220621010859363.png)

- find : 

![image-20220621011345903](JavaScript.assets/image-20220621011345903.png)

- concat : arr 뒤에 arr2를 붙이는 것.
- slice: 자르는 것

![image-20220621011457516](JavaScript.assets/image-20220621011457516.png)

- sort : 배열 순서 정리

![image-20220621012011156](JavaScript.assets/image-20220621012011156.png)

- 다만 sort로 했을 때 숫자형은 앞에서부터 받다보니 제대로 정렬이 안될수가 있다. 그런 경우, 비교 형식을 위와 하여 정렬해준다. 1은 a가 b보다 크므로 뒤에 위치한다는 뜻이다!

![image-20220621012413605](JavaScript.assets/image-20220621012413605.png)

- join : 합치기!





----



![image-20220621170548783](JavaScript.assets/image-20220621170548783.png)

- 비동기는 setTimeout을 이용하여 사용 

![image-20220621215810288](JavaScript.assets/image-20220621215810288.png)

- 콜백함수

![image-20220621225729100](JavaScript.assets/image-20220621225729100.png)

- Promise를 사용하여 콜백지옥 탈출하기