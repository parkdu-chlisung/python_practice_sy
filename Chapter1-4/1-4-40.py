# 문제 40 : 놀이동산에 가자 

maxWeight = int(input())
n = int(input())
weight = []

for i in range(0,n-1,1):
    weight[i] = int(input())

total = 0
for i in range(n):
    total += weight[i]
    if total > maxWeight:
        print(i)
        break