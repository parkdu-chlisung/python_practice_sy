# 문제 20 : 몫과 나머지
# 공백으로 구분하여 두 숫자가 주어집니다.
# 첫번째 숫자로 두번째 숫자를 나누었을 때 그 몫과 나머지를 공백으로 구분하여 출력하세요.

a,b = map(float, input().split())
print(a//b,a%b)

# 목과, 나머지를 한꺼번에 출력해주는 빌트인 함수 -> 숫자가 클때는 이게 더 성능이 좋다 
print(divmod(a,b))