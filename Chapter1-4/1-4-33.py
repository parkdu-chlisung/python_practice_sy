# 문제 33 : 거꾸로 출력하기
# 한 줄에 여러개의 숫자가 입력되면, 역순으로 그 숫자들을 하나씩 출력하는 프로그램을 작성하시오.

num = list(map(int,input().split()))
num.reverse()

for i in range(0,len(num),1):
    print(num[i], end=" ")
