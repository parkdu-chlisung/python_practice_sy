# 문제 32 : 문자열 만들기
# 취업 준비생인 원영이는 자기소개서를 쓰고 있습니다.
# 열심히 자기소개서를 작성하던 도중 원영이는 자기가 지금까지 단어를 얼마나 적었는지 궁금하게 됩니다.
# 원영이를 위해 문자열을 입력받으면 단어의 갯수를 출력하는 프로그램을 작성해 주세요.

# sentence = list(input())

# a = 0
# for i in range(0,len(sentence),1):
#     if sentence[i]==" ":
#         a += 1

# print(a+1)

# 이때의 문제점 -> 중간에 여러개의 공백이 들어가면 이상한 값이 나온다.

data = '안녕하세요        저는        박세연      입니다.'
splitData = data.split(' ')
for i in range(splitData.count('')):
    splitData.remove('')

print(splitData)

# **

