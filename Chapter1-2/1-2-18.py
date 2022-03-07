# 문제 18 : 평균 점수
# 영하네 반은 국어, 수학, 영어 시험을 보았습니다. 영하는 친구들의 평균 점수를 구해주기로 했습니다.
# 공백으로 구분하여 세 과목의 점수가 주어지면 전체 평균 점수를 구하는 프로그램을 작성하세요.
# 단, 소수점 자리를 모두 버립니다.

kor, math, eng = map(int, input().split())
total = kor + math + eng
avg = total/3
print(int(avg))

# 한 번에 값 여러 개 받기
# 변수1, 변수2 = input().split()
# 변수1, 변수2 = input().split(기준문자)
# 변수1, 변수2 = input(문자열).split()
# 변수1, 변수2 = input(문자열).split(기준문자)

# 소수점 버리니까 //로 나누면 됨.
# 엄청 간단하군
# list, map은 외우다시피 자주 사용함!

data = sum(list(map(int, input().split())))//3
data

list(map(lambda x:x**2,[10,20,30]))
# 이렇게도 사용 가능 lambda 사용해서

def 제곱(x):
    return x**2

list(map(제곱,[10,20,30]))