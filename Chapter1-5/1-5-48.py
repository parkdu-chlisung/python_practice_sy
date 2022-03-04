# 문제 48 : 대소문자 바꿔서 출력하기

abc = list(input())

for i in abc:
    if i.isupper():
        print(i.lower(),end="")
    elif i.islower:
        print(i.upper(),end="")

# for i in abc:
#     print(i,end="")
