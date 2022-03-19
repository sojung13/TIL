## 데이터 구조(Data Structure)

### 문자열(String Type)

- 문자들의 나열(sequence of characters)
  - 모든 문자는 str 타입
- 문자열은 작은 따옴표나 큰 따옴표를 활용하여 표기



> .fine(x)

: x의 첫 번째 위치를 반환. 없으면, -1을 반환함.

```python
'apple'.find('p')
# 1

```

> .index(x)

: x의 첫 번째 위치를 반환. 없으면, 오류 발생

```python
'apple'.index('p')
# 1
'apple'.index('k')
# ValueError!
```

![image-20220124155703644](데이터구조(DataStructure).assets/image-20220124155703644.png)

> .replace(old, new[,count])

바꿀 대상 글자를 새로운 글자로 바꿔서 반환.

count를 지정하면, 해당 개수만큼만 시행

```python
'woooowoo'.replace('o','!',2)
#'W!!oowoo'
```



> .strip([chars])

특정한 문자들을 지정하면, 양쪽을 제거하거나(strip), 왼쪽을 제거하거나(lstip), 오른쪽을 제거(rstrip). 문자열을 제정하지 않으면 공백을 제거함

```python
'	와우!\n'.strip()
#'와우!'
```



> .split([chars])

: 문자열을 특정한 단위로 나눠 리스트로 변환

```python
'a,b,c'.split('')
#['a','b','c']
```





> 'seperator'.join([iterable])

: 반복가능한(iterable) 컨테이너 요소들을 separator(구분자)로 합쳐 문자열 반환

```python
'!'.join('ssafy')
# s!s!a!f!y!
```

![image-20220124160213835](데이터구조(DataStructure).assets/image-20220124160213835.png)



### 리스트(List)

- 순서를 가지는 0개 이상의 객체를 참조하는 자료형
- 항상 대괄호 형태로 출력

![image-20220124160247853](데이터구조(DataStructure).assets/image-20220124160247853.png)



> .append(x)

: 리스트에 값을 추가함

```python
cafe = ['starbucks','tomntoms']
print(cafe)
cafe.append('twosome')
print(cafe)

# ['starbucks','tomntoms']
# ['starbucks','tomntoms','twosome']
```



> .extend(iterable)

: 리스트에 iterable의 항목을 추가함

```python
cafe = ['starbucks','tomntoms']
print(cafe)
cafe.extend('twosome')
print(cafe)

# ['starbucks','tomntoms']
# ['starbucks','tomntoms','t','w','o','s','o','m','e']
```



> .insert(i,x)

```python
cafe = ['starbucks','tomntoms']
print(cafe)
cafe.insert(0,'start')
print(cafe)

# ['starbucks','tomntoms']
# ['start',starbucks','tomntoms']
```



> .remove(x)

: 리스트에서 값이 x인 것 삭제

```python
numbers = [1,2,3,'hi']
print(numbers)
numbers.remove('hi')
print(numbers)

# [1,2,3,'hi']
# [1,2,3]
```



> .pop(i)

: 정해진 위치 i에 있는 값을 삭제하고, 그 항목을 반환함

: i가 지정되지 않으면, 마지막 항목을 삭제하고 반환함

```python
numbers = ['hi',1,2,3]
print(numbers)
numbers.pop()
print(numbers)

# ['hi',1,2,3]
# ['hi',1,2]
```



> .clear()

: 모든 항목을 삭제함

```python
numbers = [1,2,3]
print(numbers)
numbers.clear()
print(numbers)

# [1,2,3]
# []
```



> .index(x)

: x 값을 찾아 해당 index 값을 반환

```python
numbers = [1,2,3,4]
print(numbers)
print(numbers.index(3))
print(numbers.index(100))

# [1,2,3,4]
# 2
# 없는 경우 ValueError 반환
```



> .count(x)

: 원하는 값의 개수를 반환함

```python
numbers = [1,2,3,1,1]
numbers.count(1)
# 3

numbers = [1,2,3,1,1]
numbers.count(100)
# 0
```



> .sort()

원본 리스트를 정렬함. None 반환. sorted 함수와 비교할 것

```python
numbers = [3,2,5,1]
result = numbers.sort()
print(numbers, result())
# [1,2,3,5] None

numbers = [3,2,5,1]
result = sorted(numbers)
print(numbers, result)
# [3,2,5,1] [1,2,3,5]
```



> .reverse()

: 순서를 반대로 뒤집음(정렬하는 것이 아님)

```python
numbers = [3,2,5,1]
result = numbers.reverse()
print(numbers, result)
# [1,5,2,3] None
```







### 튜플(Tuple)

- 순서를 가지는 0개 이상의 객체를 참조하는 자료형
- 항상 소괄호 형태로 출력





### 셋(Set)

- 순서없이 0개 이상의 해시가능한 객체를 참조하는 자료형
- 담고있는 객체를 삽입 변경, 삭제 가능 > 가변자료형(mutable)
- 수학에서의 집합과 동일한 구조를 가짐

![image-20220124212442786](데이터구조(DataStructure).assets/image-20220124212442786.png)



> .add(elem)

: 셋에 값을 추가

```python
a = {'사과', '바나나', '수박'}
print(a)
a.add('딸기')
print(a)

# {'바나나','사과','수박'}
# {'바나나','사과','수박', '딸기'}
```



> .update(*others)

: 여러 값을 추가

```python
a = {'사과', '바나나', '수박'}
print(a)
a.update(['딸기','바나나','참외'])
print(a)

# {'바나나','사과','수박'}
# {'바나나', '사과','참외','수박','딸기'}
```



> .remove(elem)

: 셋에서 삭제하고, 없으면 KeyError

```python
a = {'사과', '바나나', '수박'}
print(a)
a.remove('사과')
print(a)
a.discard('청포도')
print(a)

# {'바나나','사과','수박'}
# {'바나나', '수박'}
# KeyError
```



> .discard(elem)

: 셋에서 삭제하고, 없어도 에러가 발생하지 않음

```python
a = {'사과', '바나나', '수박'}
print(a)
a.discard('사과')
print(a)
a.discard('청포도')
print(a)

# {'바나나','사과','수박'}
# {'바나나','사과'}
# {'바나나','사과'}
```



> .pop()

: 임의의 원소를 제거해 반환

```python
a = {'사과', '바나나', '수박'}
print(a)
a.pop()
print(a)

# {'사과','수박'}
```





### 딕셔너리(Dictionary)

- 순서 없이 키-값(key-value) 쌍으로 이뤄진 객체를 참조하는 자료형
- 딕셔너리의 키(key) : 해시가능한 불변 자료형만 가능
- 각 키의 값(values) : 어떠한 형태든 관계 없음

![image-20220124213214021](데이터구조(DataStructure).assets/image-20220124213214021.png)



> .get(key[,default])

- key를 통해 value를 가져옴
- KeyError가 발생하지 않으며, default 값을 설정할 수 있음(기본 : None)

```python
my_dict = {'apple':'사과','banana':'바나나'}
print(my_dict.get('Pineapple'))
print(my_dict.get('apple'))
print(my_dict.get('Pineapple',0))

# None
# 사과
# 0
```



> .pop(key[,default])

- key가 딕셔너리에 있으면 제거하고 해당 값을 반환
- 그렇지 않으면 default를 반환
- default 값이 없으면 KeyError

```python
my_dict = {'apple':'사과','banana':'바나나'}
data = my_dict.pop('apple')
print(data, my_dict)

# 사과 {'banana':'바나나'}
```



> .update()

: 값을 제공하는 key, value로 덮어쓴다

```python
my_dict = {'apple':'사','banana':'바나나'}
my_dict.update(apple='사과')
print(my_dict)

# {'apple':'사과','banana':'바나나'}
```





### 얕은 복사과 깊은 복사(Shallow Copy & Deep Copy)

> 할당(Assignment)

- 대입 연산자(=) : 리스트 복사 확인하기

```python
original_list = [1,2,3]
copy_list = original_list
print(original_list,copy_list)

# [1,2,3] [1,2,3]

copy_list[0] = "hello"
print(original_list, copy_list)

# ['hello',2,3] ['hello',2,3]
```



> 얕은 복사(Shallow copy)

- Slice 연산자를 이용하여 같은 원소를 가진 리스트지만 연산된 결과를 복사

```python
a = [1,2,3]
b = a[:]
print(a,b)
b[0]=5
print(a,b)

# [1,2,3] [1,2,3]
# [1,2,3] [5,2,3]
```



> 깊은 복사(Deep copy)

```python
import copy
a = [1,2,['a','b']]
b = copy.deepcopy(a)
print(a,b)
b[2][0] = 0
print(a,b)

# [1,2,['a','b']] [1,2,['a','b']]
# [1,2,['a','b']] [1,2,[0,'b']]
```

