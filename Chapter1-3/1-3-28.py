# 문제 28 : 2-gram
# 2-gram이란 문자열에서 2개의 연속된 요소를 출력하는 방법입니다.
# 예를 들어, 'Python'을 2gram으로 반복해본다면 다음과 같은 결과가 나옵니다.
# Py
# yh
# th
# ho
# on
# 입력으로 문자열이 주어지면 2-gram 으로 출력하는 프로그램을 작성해주세요. 

word = list(input())
for i in range(0, len(word)-1, 1):
    print(word[i], end="")
    print(word[i+1])