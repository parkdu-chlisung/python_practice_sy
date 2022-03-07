# 문제 4 : 변수의 타입 2
# 다음 변수 a를 print(type(a))로 넣었을 때 출력될 값과의 연결이 알맞지 않은 것은>

# 1) 입력 : a = 1, 출력 : class 'int;
# 2) 입력 : a = 2.22, 출력 : class 'float';
# 3) 입력 : a = 'p', 출력 : class 'char';
# 4) 입력 : a = [1,2,3], 출력 : class 'list';

a = 1
print(type(a))
b = 2.22
print(type(b))
c = 'p'
print(type(c))
d = [1,2,3]
print(type(d))

# 3번 
# 파이썬에는 C, C# 등에서 존재하는 문자(char) 타입이 존재하지 않는다.
#  따라서, char가 아닌 문자열 str 타입이 된다.

# 홑따옴표나, 쌍 따옴표가 붙으면 string
# 대괄호로 감싸져 있으면, list