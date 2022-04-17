## Database

> 데이터베이스(DB)

- 데이터베이스는 `체계화된 데이터`의 모임
- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
- 논리적으로 연관된 (하나 이상의) 자료의 모음으로 그 내용을 고도로 구조화 함으로써 검색과 갱신의 효율화를 꾀한 것
- 즉, `몇 개의 자료 파일을 조직적으로 통합`하여 `자료 항목의 중복을 없애`고 `자료를 구조화하여 기억`시켜 놓은 `자료의 집합체`



> 관계형 데이터베이스(RDB)

- Relational Database
- 키(Key)와 값(Value)들의 간단한 관계(relation)를 표(table) 형태로 정리한 데이터베이스



> 관계형 데이터베이스 용어 정리

✔️ `스키마` : 데이터베이스에서 자료의 구조, 표현방법, 관계 등 전반적인 명세를 기술한 것.

✔️ `테이블` : 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합

✔️ `열` : 각 열에는 고유한 데이터 형식이 지정됨. 열/ 컬럼/ 필드 등의 이름으로 불림(ex. name, address, age)

✔️ `행` : 실제 데이터가 저장되는 형태. 행/ 로우/ 레코드 등의 이름으로 불림. (ex. 홍길동, 제주, 20)

✔️ `기본키` : 각 행(레코드)의 고유 값. 반드시 설정해야 하며, 데이터베이스 관리 및 관계 설정 시 주요하게 활용됨 



> SQLite

: 서버 형태가 아닌 파일 형식으로 응용 프로그램에 넣어서 사용하는 `비교적 가벼운 데이터베이스`



----



## SQL

> SQL

- 관계형 데이터베이스 관리시스템의 `데이터 관리`를 위해 설계된 `특수 목적으로 프로그래밍 언어`
- 데이터베이스 스키마 생성 및 수정
- 자료의 검색 및 관리
- 데이터베이스 객체 접근 조정 관리



> SQL 분류

![image-20220314162353518](SQL.assets/image-20220314162353518.png)

- INSERT : 새로운 데이터 삽입(추가)
- SELECT : 저장되어있는 데이터 조회
- UPDATE : 저장되어있는 데이터 갱신
- DELETE : 저장되어있는 데이터 삭제



> 테이블 생성 및 삭제

```python
$ sqlite3 tutorial.sqlite3
sqlite> .database
```

`.`은 sqlite 프로그램 기능을 실행하는 것



> csv 파일을 table로 만들기

```python
sqlite> .mode csv
sqlite> .import hellodb.csv examples
sqlite> .tables
exampltes
```



> SELECT

```python
SELECT * FROM examples;
1,"길동","홍",600,"충청도",010-0000-0000
```

SELECT 문은 특정 테이블의 레코드(행) 정보를 반환!



> 테이블 생성 및 삭제 statement

`CREATE TABLE` : 데이터베이스에서 테이블 생성

`DROP TABLE` : 데이터베이스에서 테이블 제거

```python
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT
);

sqlite> .tables
classmates examples

----

DROP TABLE classmates;
```



> 특정 테이블의 schema 조회

```python
sqlite> .schema classmates
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT
);
```



> 
