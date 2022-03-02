# 문제 16 : 로꾸꺼
# 문장이 입력되면 거꾸로 출력하는 프로그램을 만들어 봅시다.

n = input()
word = list(n)
word.reverse()

for i in range(0,len(word),1):
    print(word[i], end="")