## HTML(Hyper Text Markup Language)

- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어 
- 웹 페이지를 작성(구조화)하기 위한 언어



> HTML 기본 구조

- html : 문서의 최상위(root) 요소
- head : 문서 메타데이터 요소
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용
- body : 문서 본문 요소
  - 실제 화면 구성과 관련된 내용

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Doucment</title>
</head>
<body>
</body>
</html>
```



> head 예시

```html
< title > : 브라우저 상단 타이틀
< meta > : 문서 레벨 메타데이터 요소
< link > : 외부 리소스 연결 요소(CSS 파일, favicon 등)
< script > : 스크립트 요소(JavaScript 파일/ 코드)
< style > : CSS 직접 작성
```

```html
<head>
    <title>HTML 수업</title>
    <meta charset="UTF-8">
    <link ref="style.css" rel="stylesheet">
    <script src="javascript.js"></script>
    <style>
        p {
            color: black;
        }
    </style>
</head>
```



> 요소(element)

- HTML 요소는 시작 태그와 조율 태그 그리고 태그 사이에 위치한 내용으로 구성
  - 태그(element,요소)는 컨텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미를 정의
- 내용이 없는 태그들
  - br, hr, img, input, link, meta
- 요소는 중첩(nested)될 수 있음
  - 요소의 중첩을 통해 하나의 문서를 구조화
  - 여는 태그와 닫는 태그의 쌍을 잘 확인해야함
    - 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력되기 때문에, 디버깅이 힘들어질 수 있음



> 속성(attribute)

- 속성을 통해 태그의 부가적인 정보를 설정할 수 있음
- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
- 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재
- 태그와 상관없이 사용 가능한 속성(HTML Global Attribute)들도 있음



> HTML Global Attribute

모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성(몇몇 요소에는 아무 효과가 없을 수 있음)

```html
<id> 문서 전체에서 유일한 고유 식별자 지정 </id>
<class> 공백으로 구분된 해당 요소의 클래스의 목록(CSS, JS에서 요소를 선택하거나 접근</class>
<data> 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용 </data>
<style> inline 스타일 </style>
<title> 요소에 대한 추가 정보 지정 </title>
<tabindex> 요소의 탭 순서 </tabindex>
```



> 시맨틱 태그

- HTML5에서 의미론적 요소를 담은 태그의 등장
  - 기존 영역을 의미하는 div 태그를 대체하여 사용
- 대표적인 태그 목록

```html
<header> 문서 전체나 섹션의 헤더(머리말 부분) </header>
<nav> 내비게이션 </nav>
<aside> 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠 </aside>
<section> 문서의 일반적인 구분, 콘텐츠의 그룹을 표현 </section>
<article> 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역 </article>
<footer> 문서 전체나 섹션의 푸터(마지막 부분) </footer>
```

- Non semantic 요소는 div, span 등이 있으며 h1, table 태그들도 시맨틱 태그로 볼 수 있음
- 개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미 있는 정보의 그룹을 태그로 표현
- 단순히 구역을 나눈 것 뿐만 아니라 '의미'를 가지는 태그들을 활용하기 위한 노력
- 요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수를 쉽게 함
- 검색엔진최적화(SEO)를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 활용해야함



>  텍스트 요소

```html
<a> href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성 </a>
<b> 굵은 글씨 요소</b>
* <strong> 중요한 강조하고자 하는 요소(보통 굵은 글씨로 표현) </strong>
<i> 기울임 글씨 요소 </i>
* <em> 중요한 강조하고자 하는 요소(보통 기울임 글씨로 표현) </em>
<br> 텍스트 내에 줄 바꿈 생성
<img> src 속성을 활용하여 이미지 표현
<span> 의미 없는 인라인 컨테이너 </span>

* - 시맨틱 태그
```



> 그룹 콘텐츠

```html
<p> 하나의 문단 </p>
<hr> 문단 레벨 요소에서의 주제의 분리를 의미하며 수평선으로 표현됨
<ol></ol> 순서가 있는 리스트(ordered)
<ul></ul> 순서가 없는 리스트(unordered)
<pre> HTML에 작성한 내용을 그대로 표현. 보통 고정폭 글꼴이 사용되고 공백문자를 유지</pre>
<blockquote> 텍스트가 긴 인용문. 주로 들여쓰기를 한 것으로 표현됨 </blockquote>
<div> 의미 없는 블록 레벨 컨테이너 </div>
```



> table

table의 각 영역을 명시하기 위해 <thead> <tbody> <tfoot> 요소를 활용![image-20220203123527490](HTML.assets/image-20220203123527490.png)





> form > Django에서 굉장히 자주 사용

- < form >은 정보(데이터)를 서버에 제출하기 위한 영역

- < form>기본속성
  - action : form을 처리할 때의 URL
  - method : form을 제출할 때 사용할 HTTP 메서드(GET 혹은 POST)
  - enctype : method가 post인 경우 데이터의 유형
    - application/ x-www-form-urlencoded : 기본값
    - multipart/ form-data : 파일 전송시 (input type이 file인 경우)



> input

- 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
- < input > 대표적인 속성
  - name : form control에 적용되는 이름(이름/ 값 페어로 전송됨)
  - value : form control에 적용되는 값(이름/ 값 페어로 전송됨)
  - required, readonly, autofocus, autocomplete, disabled 등



> input label

- label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음
  - 사용자는 선택할 수 있는 영역이 늘어나 웹/ 모바일(터치) 환경에서 편하게 사용할 수 있음
  - label과 input 입력의 관계가 시각적 뿐만 아니라 화면리더기에서도 label을 읽어 쉽게 내용을 확인할수 있도록 함
  - < input >에 id 속성을, < label >에는 for 속성을 활용하여 상호 연관을 시킴

```html
<label for "agreement">개인정보 수집에 동의합니다.</label>
<input type="checkbox" name="agreement" id"agreement>
```



> input 유형 - 일반

일반적으로 입력을 받기 위하여 제공되며 타입별로 HTML 기본검증 혹은 추가 속성을 활용할수 있다. 

- text : 일반 텍스트 입력
- password : 입력시 값이 보이지 않고 문자를 특수기호(*)로 표현
- email : 이메일 형식이 아닌 경우 form 제출 불가
- number : min, max, step 속성을 활용하여 숫자 범위 설정 가능
- file : accept 속성을 활용하여 파일 타입 지정 가능

![image-20220203190242743](HTML.assets/image-20220203190242743.png)



- 동일 항목에 대하여는 name을 지정하고 선택된 항목에 대한 value를 지정해야 함
  - checkbox : 다중선택
  - radio : 단일 선택

![image-20220203190332498](HTML.assets/image-20220203190332498.png)

- 다양한 종류의 input을 위한 picker를 제공
  - color : color picker
  - date : date picker

![image-20220203190832861](HTML.assets/image-20220203190832861.png)

- hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
  - hidden : 사용자에게 보이지 않는 input





----



## CSS

= 스타일을 지정하기 위한 언어

![image-20220203190908825](HTML.assets/image-20220203190908825.png)

- CSS 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미.
  - 속성(Property) : 어떤 스타일 기능을 변경할지 결정
  - 값(Value) : 어떻게 스타일 기능을 변경할지 결정



> CSS 정의 방법

1. 인라인(inline) : 해당 태그에 직접 style 속성을 활용
2. 내부 참조(embedding) - <style> : < head> 태그 내에 <style>에 지정
3. 외부 참조(link file) - 분리된 CSS 파일



> 선택자(Selector) 유형

- 기본 선택자
  - 전체 선택자, 요소 선택자
  - 클래스 선택자, 아이디 선택자, 속성 선택자
- 결합자(Combinators)
  - 자손 결합자, 자식 결합자
  - 일반 형제 결합자, 인접 형제 결합자
- 의사 클래스/요소(Pseudo Class)
  - 링크, 동적 의사 클래스
  - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자



> CSS 선택자 정리

- 요소 선택자 : HTML 태그를 직접 선택
- 클래스(class) 선택자 : 마침표(.) 문자로 시작하며, 해당 클래스가 적용된 항목을 선택
- 아이디(id) 선택자 : # 문자로 시작하며, 해당 아이디가 적용된 항목을 선택. 일반적으로 하나의 문서에 1번만 사용. 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장



> CSS 적용 우선순위(cascading order)

1. 중요도(Importance)- 사용시 주의
   - ! important
2. 우선순위(Specificity)
   - 인라인> id> class, 속성, pseudo-class> 요소, pseudo-element
3. CSS 파일 로딩 순서



> CSS 상속

CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.

- 속성(프로퍼티)중에는 상속이 되는 것과 되지 않는 것들이 있다.
- 상속 되는 것 예시
  - 예) Text 관련 요소(font, color, text-align), opacity, visibility 등
- 상속 되지 않는 것 예시
  - 예) Box model 관련 요소(width, height, margin, padding, border, box-sizing, display), position 관련 요소(position, top/right/bottom/left, z-index) 등



> 크기 단위

- px(픽셀)
  - 모니터 해상도의 한 화소인 픽셀 기준
  - 픽셀의 크기는 변하지 않기 떄문에 고정적인 단위
- %
  - 백분율 단위
  - 가변적인 레이아웃에서 자주 사용

- em
  - (바로 위, 부모 요소에 대한) 상속의 영향을 받음
  - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
- rem 
  - (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
  - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐
- viewport
  - 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 콘텐츠의 영역(디바이스 화면)
  - 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
  - vw, vh, vmin, vmax



> 색상 단위

- 색상 키워드
  - 대소문자를 구분하지 않음
  - red, blue, black과 같은 특정 색을 직접 글자로 나타냄
- RGB 색상
  - 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현하는 방식
  - '#' + 16진수 표기법
  - rgb() 함수형 표기법
- HSL 색상
  - 색상, 채도, 명도를 통해 특정 색을 표현하는 방식
  - a는 alpha(투명도)



> 결합자(Combinators)

- 자손 결합자
  - selectorA 하위의 모든 selectorB의 요소
- 자식 결합자
  - selectorA 바로 아래의 selectorB의 요소

![image-20220203192831676](HTML.assets/image-20220203192831676.png)

- 일반 형제 결합자
  - selectorA의 형제 요소 중 뒤의 위치하는 selectorB 요소를 모두 선택
- 인접 형제 결합자
  - selectorA의 형제 요소 중 바로 뒤에 위치하는 selectorB 요소를 선택







![image-20220203192926836](HTML.assets/image-20220203192926836.png)

모든 요소는 네모(박스모델)이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다

![image-20220203192954924](HTML.assets/image-20220203192954924.png)

![image-20220203193043312](HTML.assets/image-20220203193043312.png)

> box-sizing

- 기본적으로 모든 요소의 box-sizing은 content-box
  - Padding을 제외한 순수 contents 영역만을 box로 지정
- 다만, 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100 px로 보는 것을 원함(width를 100으로 설정하였을 때)
  - 그 경우 box-sizing을 border-box로 설정

![image-20220203194430314](HTML.assets/image-20220203194430314.png)



### CSS Display

- display : block
  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체의 가로 폭을 차지한다.
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음.
  - 대표적인 블록 레벨 요소
    - div / ul, ol, li/ p / hr / form 등
- display : inline
  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  - content 너비만큼 가로 폭을 차지한다.
  - width, height, margin-top, margin-bottom을 지정할 수 없다.
  - 상하 여백은 line-height로 지정한다.
  - 대표적인 인라인 레벨 요소
    - span / a / img / input, label / b, em, i ,strong 등

![image-20220203194750416](HTML.assets/image-20220203194750416.png)

- display : inline-block
  - block과 inline 레벨 요소의 특징을 모두 가짐
  - inline처럼 한 줄에 표시 가능하고, block처럼 width, height, margin 속성을 모두 지정할 수 있다.
- display : none
  - 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
  - 이와 비슷한 visibility : hidden은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다.



> CSS position

- 문서 상에서 요소를 위치를 지정
- static : 모든 태그의 기본 값(기준 위치)
  - 일반적인 요소의 배치 순서에 따름(좌측 상단)
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치됨
- 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
  - relative
  - absolute
  - fixed





- relative : 상대 위치

  - 자기 자신의 static 위치를 기준으로 이동(normal flow 유지)
  - 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음(normal position 대비 offset)
  - 본인의 원래 위치를 기준

  ![image-20220203195322653](HTML.assets/image-20220203195322653.png)



- absolute : 절대 위치
  - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
  - static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(없는 경우 body)
  - 특정 부모의 위치를 기준

![image-20220203195342717](HTML.assets/image-20220203195342717.png)

![image-20220203195633036](HTML.assets/image-20220203195633036.png)

- fixed : 고정 위치
  - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
  - 부모 요소와 관계없이 viewport를 기준으로 이동
    - 스크롤 시에도 항상 같은 곳에 위치함 like 광고!

![image-20220203195413793](HTML.assets/image-20220203195413793.png)
