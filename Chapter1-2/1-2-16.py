# 문제 16 : 로꾸꺼
# 문장이 입력되면 거꾸로 출력하는 프로그램을 만들어 봅시다.

# n = input()
# word = list(n)
# word.reverse()

# for i in range(0,len(word),1):
#     print(word[i], end="")


# 가장 쉬운 방법
from tkinter import E


문자열 = input()
print(문자열[::-1])

# 반복문 사용
s = ''
for i in 문자열 :
    s = i + s # 이렇게 순서를 바꾸면 역순으로 출력된다.** 이유는 모르겟음,,
    # s += s 즉, s = s + i 하면 순서대로 출력됨
print(s)

# 재귀함수 사용**
def 거꾸로(s):
    if len(s) == 1 :
        return s
    else :
        return 거꾸로(s[1:]) + s[0]
        # 이것두 순서 바꾸면 순서대로 출력 됨

print(거꾸로(문자열))