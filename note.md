
# python note

## 💛BOOKMARK
| 주제 | 내용 | 난이도 | 메모 |
|:----------:|:----------:|:----------:|:----------:|
| [출력](#출력) | format용법 | ⭐️ |
| [숫자자료형](#숫자자료형) | id, is, == | ⭐️ |
| [문자자료형](#문자자료형) | 문자메소드 | ⭐️⭐️ |
| [형변환](#형변환) | 문자메소드 | ⭐️ |
| [True Or False](#TureOrFalse) | True 혹은 False를 반환시 주의할 것들 | ⭐️⭐️⭐️ |
| [연산](#연산) | 연산기호 | ⭐️ |
| [지역변수와 전역변수](#지역변수와전역변수) | 지역변수 global | ⭐️⭐️ |
| [리스트](#리스트) | 내장메소드, 리스트표현식 | ⭐️⭐️ |
| [튜플](#튜플) | 튜플의 특징 | ⭐️⭐️ |
| [딕셔너리](#딕셔너리) | 딕셔너리 특징, 메소드, 선언방법 | ⭐️⭐️ |
| [셋](#셋) | 메소드 | ⭐️⭐️⭐️ |
| [조건문](#조건문) | if | ⭐️ |
| [반복문](#반복문) | for, break, continue, pass, while | ⭐️⭐️ |
| [리스트표현식](#리스트표현식) |  | ⭐️⭐️⭐️⭐️ |


---

### 출력
- format 용법
    ```python
    print('{0} X {1} = {2}'.format(a,b,a*b))
    ```
- 추가된 기능
    ```python
    print(f'{변수명}')
    ```


### 숫자자료형 
- 최댓값, 최솟값 존재 X 
- 자동으로 메모리 할당
- id(변수명) -> 메모리의 주소 값
    - (256까지는) 같은 숫자가 저장되어있다면, 메모리 주소 값이 같다.
    - 257부터는 같은 숫자가 저장되어있더라도 메모리 주소 값이 다르다.
    - id값이 같으면 **a is b**는 **True**이다.
    - 값이 같지만, id값이 다르면 **a==b**는 **True**이지만, **a is b**는 **False**이다.
- 실수 계산이 부정확함

### 문자자료형
- 순서가 있는 시퀀스형 자료형
- 슬라이싱 
    - s [ start : stop : step ]
- 문자 메소드
    - s.lower() : 전체 소문자로
    - s.upper() : 전체 대문자로
    - s.find('a') : a가 몇번째 index에 존재하나, 없으면 -1 return
    - s.index('a') : a가 몇번째 index에 존재하나, 없으면 error
    - s.count('a') : a의 개수
    - s.stript() : 양쪽 공백 삭제 
        - s.stript(' ,!') : 공백, 컴마, 느낌표 모두 같이 없어짐
    - s.replace('a','A') : a를 A로 교체  
        - 메서드 체이닝 가능
    - s.split(' ') : 공백 단위로 자른다.
    - s.join('~') : ~ 단위로 합친다.
    - s.isalnum() : 숫자인가요
    - s.isalpha() : 문자인가요
    - s.rjust(30) : 30자로 맞추기
    - s.center(30) : 중앙정렬 (30이 문자수보다 적으면, 그냥 문자 그대로 반환)
    - s.zfill(30) : 나머지를 0으로 채우기
    - s.translate(규칙테이블)
    - 문자 자료형 출력
        ```python
        print('{} X {} = {}'.format(2,3,6))
        # 4칸으로 출력
        print('{0:4} X {1:4} = {2:4}'.format(2,3,6)
        # < 왼쪽 정렬, ^ 가운데 정렬, > 오른쪽 정렬
        print('{0:<4} X {1:^4} = {2:>4}'.format(2,3,6))
        ```
### 형변환
- 자료형(변수)

### TureOrFalse
- **0 : False**
- 0 이외의 숫자 : True
- 공백 : True 
    - bool('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;')
- **아무것도 없는 문자열 : False**
    - bool('')
- bool(None) : True
- 빈 리스트 : False
    - bool([])
    - 주의 ) **bool([0])은 True**
- 빈 Tuple : False
    - bool(())
    - 주의 ) **bool((0))은 False**

### 연산
- xor : 다를때 1, 같을때 0

### 함수
```python
def function():
    ```
    함수 설명
    ```
print(function.__doc__) # 함수설명 출력
help(function) # 함수설명 출력
```
- return 2개 이상 가능

## 지역변수와전역변수
- 전역변수 global
- List는 global로 호출하지 않아도 됨

## 리스트
- 순서가 있는 시퀀스형 자료형
- 리스트 내장 메소드
    - l.append(10) : 10을 붙이기
        ```python
        print(l.append(10)) 
        # return 값은 None이다. 왜냐면 append는 리턴값이 없이 값을 붙여만 주는 함수이기에
        ```
    - l.clear() : 모두 삭제 
    - l.copy() : 값을 복사한다. 원본의 값은 바뀌지 않음.
    - l.count(1) : 리스트 안의 1의 개수를 출력해준다.
    - l.extend([1,2,3]) : 리스트 뒤에 1,2,3 추가
        - 주의 ) append는 안된다.
            - l.append(1,2,3,4) -> 여러개 하면 에러남
            - l.append([1,2,3]) -> 에러는 안나는데 2차원 행렬이 된다.
    - l.index(5) : 5가 몇번째 index인지를 출력
    - l.insert('1', '5') : 1번 index에 5를 삽입
    - l.pop() : 맨 마지막 값을 return 하고 삭제
    - l.pop('index') : index번째 값을 꺼내 return하고 삭제
    - l.remove('1') : 1을 삭제(첫번쨰로 만난 1만 삭제)
    - l.reverse() : 저장된 순서의 역순으로
    - l.sort() : 크기순으로 정렬한다.
    - 주의 ) sorted(l) -> 정렬된 값이 리턴된다. 단, return값만 정렬된다.
    - 주의 ) reversed(l) -> 역순된 값이 리턴된다. 단, return값만 정렬된다.
        - list(reversed(l)) -> 형변환 해야함
- 리스트 표현식
    ```python
    l = [1,2,3,4,5]
    l = [i for i in range(1,100)]
    l = [i for i in range(1,100) if i % 3 == 0 or i % 5 == 0]
    ```

### 튜플
- 순서가 있는 시퀀스형 자료형 (이 점은 리스트와 동일)
- 참조값의 변경이 불가능함 (리스트와의 차이점)
- 변경이 불가능하기에 append, extend 불가능

### 딕셔너리
- 순서가 없는 자료형 -> 최신 버젼에서는 순서 있는듯
- 키와 값으로 이루어져 있음
- 값의 변경 가능, 다른 자료형 입력 가능
- 키의 중복 허락 X, 값의 중복은 허락 O
    - 키가 중복되면, 마지막에 쓰인 것으로 들어간다.
```python
dict([('one','하나') , ('two','둘')])
dict(name = '세연' , age = '22')
dict(zip('ABC', '123'))
# {'A' : '1' , 'B' : '2' , 'C' : '3'}
```
- 메소드 
    - d.keys() : 키들만 출력
    - d.values() : 값들만 출력
    - d.itmes() : 키와 값들을 맵핑하여 출력
    - d.fromkeys()
    - d.update({'a':'100', 'b' :'200'})
    - d.del['a']
- 딕셔너리 출력
    ```python
    for i in d:
        print(i) # key값만 출력
    for i in d :
        print(i, d[i]) # 같이 출력
    for i,j in d.items():
        print(i,j) # 같이 출력

### 셋
- 메소드
    - s.add(5) : 5를 추가
    - s.update('123')
        - s.update({1,2,3})
        - s.update([1,2,3])
        - 주의 ) s.update(6) -> 이건 에러남
    - s.difference(ss) : s - ss
    - s.intersection(ss) : s && ss (교집합)
    - set.union(s,ss) : s | ss (합집합)
    - s.remove(1) : 1 삭제, 1이 없을시에 에러
    - s.discard(1) : 1 삭제, 1이 없을시에 에러안남
    - s.pop()
    - s.issubset({1,2}) : {1,2} 안에 s가 속하니
    - s.isdisjoint(ss) : 겹치는 부분이 있냐 없냐

### 조건문
```python
if True :
    # 들여쓰기로 구분
```
    
### 반복문
```python
for i in [10,20,30]:
    # i는 반복해서 받을 변수명
    # in 뒤에는 순회할 Object
```
- break : 반복문 빠져나옴
- continue : 다음 for문으로 넘어가라 (continue 밑은 실행하기 않고 넘어감)
- pass : 있으나마나

### 리스트표현식
