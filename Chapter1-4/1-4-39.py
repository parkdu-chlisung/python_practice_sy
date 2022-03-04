# 문제 39 : 오타 수정하기

word = list(input())
for i in range(len(word)):
    if word[i] == 'q':
        word[i] = 'e'

for i in range(len(word)):
    print(word[i], end="")