Built in Functions

abs
all
any

이건 잘 안나옴 

dir([1,2,3])
하면 리스트의 메서드들이 나온다.

format(100000000,',')
컴마로 끊어준다.

format(100000,'!>020,.4f')
!로 채워주고, 오른쪽 정렬에 20자리까지 소수점은 4자리까지

def function(value):
    if value%2 == 0:
        return True
    else
        return False

list(filter(function, range(20)))
어떤 값들을 특정 function으로 필터를 줄 때 사용한다.

-> 이걸 람다로 표현 가능

list(filter(lambda x : x % 2 == 0, range(20)))
결과는 같음

-> 리스트 표현식으로도 가능
[i for i in range(20) if i % 2 == 0]

len([1,2,3,4]) : 길이를 반환한다.

list(map(function, range(20)))
-> 이렇게하면 Ture나 False가 나옴
-> filter는 Ture에 해당하는 값을 가져오는데..

list(map(lambda x : x % 2 == 0, range(20)))
list(zip(['a','b','c','d'],[1,2,3,4]))

map과 zip은 자주 사용하니 기억하기

max([1,2,3,4]) : 최댓값
min([1,2,3,4]) : 최솟값

reversed() -> 역순 (역정렬은 아님)
sorted()
-> 리스트를 직접 만지지 않는다. 리턴 값만 정렬 된 값이다.

*이거랑 비교할 빌트인펑션
l = [10,5,4,3,7,6]
l.sort() 
-> sort()는 리스트를 직접 만진다.

testCaseOne = ['abc', 'def', 'hello world', 'hello','python']
testCaseTwo = 'Life if too short, You need python'.split()
testCaseThree = list(zip('anvfe',[1,2,5,4,3]))

sorted(testCaseOne, key=len, reverse=True)
-> reverse안하면 길이별로 정렬됨
-> reverse=True해서 길이별 역순으로 정렬됨

sorted(testCaseTwo, key=str.lower)
-> 대소문자 구별없이, 알파벳 순으로

sorted(testCaseThree, key=lambda x:x[1])
-> x값의 1번째 값으로 정렬해라 (이 예제에서는 숫자로 정렬하겠지요)

5 in [1,2,3,4,5]
in 많이 사용
not in도 많이 사용

리스트의 메소드를 살펴보겠음
append 하나의 요소만 추가
clear 모든 요소를 다 없애기
copy 복사
count 개수세기
extend 여러개 요소 추가
index
insert
pop
remove 보다는 del이 효율적
reverse
sort

l = []
l.append(10)
l.append(20)
l.append(30)
l.pop(0) -> 0번째가 pop되니까 가장 먼저 들어온게 나가는거니까 queue의 구조
l.pop() -> 이렇게 되면 제일 뒤에꺼가 나가는 거니까 stack의 구조이다.

d = {'one' : '하나' , 'two' : '둘'}
자주쓰는거
d.keys()
d.values()
d.items() : 리스트 안의 튜플로 뽑아내라

del도 자주쓴다 -> 효율이 좋음

set은 중복을 제거하는 용도로 많이 쓴다.
순서가 없어서 순회를 할때 주의해야함

s.add(7) : 요소 추가
s.discard(7) : 요소 삭제
s.difference(ss) : 차집합
s.union
in 자주 사용

판콜에이 = {'A', 'B', 'C'}
타이레놀 = {'A','B','D'}
print(판콜에이.difference(타이레놀))
-> 판콜에이 - 타이레놀 = 'C'
print(판콜에이.intersection(타이레놀))
-> 교집합이니까 'A','B' (순서는 없음)
print(판콜에이.union(타이레놀))
-> 합집합 


리스트에 있는 숫자문자를 int로 바꾸는법
for i in '1 2 3 4 5 6 7'.split():
    print(int(i))

[int(i) for i in '1 2 3 4 5 6'.split()]

list(map(int, '1 2 3 4 5'.split()))
-> 가장 효율적

단톡방에 x마리의 동물이 대화중
각가의 동물들이 톡을 전송할 때 마다 서버에는 아래와 같이 저장
1. 단톡방에는 모두 몇 마리의 동물이 있나. 톡은 무조건 1회 이상 전송함
2. 단톡방에는 동물들마다 몇 번의 톡을 올렸을까
serverDate = '개리 라이캣 개리 개리 라이캣 자바독 자바독 파이 썬'

len(set(serverData.split()))
-> 1번 문제 해결

d = {}
for i in set(serverData.split()):
    print(i, serverData.split().count(i))