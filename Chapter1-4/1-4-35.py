# 문제 35 : Factory 함수 사용하기
# 2제곱, 3제곱, 4제곱을 할 수 있는 Factory 함수를 만드려고 합니다.
# <pass>에 코드를 작성하여 two 함수를 완성하세요.

def one(n):
    def two():
        #<pass>
        return lambda x : x**n
    return two

# a = one(2)
# b = one(3)
# c = one(4)
# print(a(10))
# print(b(10))
# print(c(10))

# factory 함수 모르겠다