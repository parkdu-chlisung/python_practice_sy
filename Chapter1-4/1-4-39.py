# 문제 39 : 오타 수정하기

# word = list(input())
# for i in range(len(word)):
#     if word[i] == 'q':
#         word[i] = 'e'

# for i in range(len(word)):
#     print(word[i], end="")

data = input()
print(data.replace('q','e').replace('b','n'))

# 정규표현식 사용해도됨 -> 아직.. 모름