### CLI(Command Line Interface)



`~` : 홈 디렉토리(현재 로그인된 사용자의 홈 폴더를 의미. 브라우저의 홈 화면과 같다.) 

`/` : 루트 디렉토리(모든  파일과 폴더를 담고 있는 최상의 폴더를 의미)

윈도우의 최상위 루트 디렉토리는? C 드라이브!



>  절대 경로 : (ex. 3조 3열) / (ex. A/B/F)
>
> 어떤 위치에서도 접근할 수 있는 경로(모든 경로를 전부 작성)

> 상대 경로 : (ex. g의 뒷자리/ e의 옆자리) 특정 기준점을 기준으로 자리를 파악
>
> 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 경로



`.` : 현재 작업하는 위치

`..` : 현재 작업하는 위치의 상위 위치(상위폴더/ 부모폴더)

GUI 기준(뿌리 구조) : (ex. ./F) 여기서 . 하나는 현재 위치 의미. 타고 올라가는 것은 ../A/B/F

절대 경로 : A/B/F



#### 터미널 명령어

`touch` : 파일 생성 명령어

```
$ touch 파일명
```



#### 폴더 생성

`mkdir` : 폴더 생성 명령어

```
$ mkdir 폴더명

$ mkdir '폴더명을 띄워쓰고 싶을 때 따옴표로 작성'

$ mkdir 폴더의 경로를/ 상대 경로로/ 지정할 수 있음
```



#### 파일/폴더의 목록 확인

`ls` : 현재 위치의 폴더 파일의 목록을 보고 싶을 때 사용하는 명령어

`-a` : 접근 가능한 모든 폴더와 파일을 확인할 때

`-l` : 자세한 정보까지 확인하고 싶을 때

```
$ ls
```



#### 파일/폴더 이동하기

`mv` : 폴더/파일을 다른 위치로 이동하거나 이름 변경할 때 사용

```
$ mv 이동하려는 파일명 이동하는 위치

$ mv 이름 변경하려는 파일명 변경하려는 이름

- 위에 두 방식이 같아보인다?! 하지만 변경하려는 이름이 폴더 안에 없을 때는 이름을 변경시켜주고, 있을때 파일을 이동시켜주는 것이다.
```



#### 현재 위치 이동하기

`cd` : 현재 위치를 이동하기 위한 명령어(Change Directory)

```
$ cd 이동할 위치
```



#### 폴더/파일 삭제

`rm` : 폴더/파일 삭제하는 명령어

```
$ rm 삭제하려는 파일명

$ rm -r 삭제하려는 폴더명

$ rm -rf 폴더명 : 폴더 무조건 삭제(강제삭제)

- 주의할 점 : CLI에는 휴지통 개념이 없다! 즉, 되 살 릴 수 없 다 !
```



#### 폴더/파일 열기

`start` : 폴더/파일을 여는 명령어

`code` : 비주얼 스튜디오 열리는 명령어



#### ☆☆☆☆☆꿀 같은 단축키☆☆☆☆☆

`위, 아래 방향키` : 과거에 작성한 명령어를 조회

`tab 키` : 자동완성

`ctrl + l` : 화면 클리어

`ctrl + insert` : 복사(ctrl + c)

`shift + insert` : 붙여넣기(ctrl + v)