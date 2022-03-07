# 문제 40 : 놀이동산에 가자 

maxWeight = float(input())
n = int(input())
weight = []
total = 0
answer = 0
비교 = True

for i in range(n):
    weight.append(float(input()))
    total += weight[i]
    if total > maxWeight:
        if 비교 :
            비교 = False
            answer = i

if answer == 0 and weight[0] <= maxWeight:
    print(len(weight))
else:
    print(answer)

# **
# 여러가지 경우의 수 생각하기
# 처음에 max보다 큰 수가 들어오거나.. -> 이때는 0명
# 딱 알맞게 탔거나 -> 인원수 출력
