# 문제 34 : sort 구현하기
# 민주는 체육부장으로 체육시간이 되면 반 친구들이 제대로 키 순서대로 모였는지를 확인해야 한다.
# 그런데 요즘 민주는 그것이 너무 번거롭게 느껴져 한 번에 확인하고 싶어한다.
# 민주를 위해 키가 주어지면 순서대로 제대로 섰는지 확인하는 프로그램을 작성해보자.

from os import TMP_MAX


height = [int(x) for x in input().split()]

tmp = 0
for i in range(0,len(height)-1,1):
    if height[i] > height[i+1]:
        height[i] = tmp
        tmp = height[i+1]
        height[i+1] = tmp
        print("NO")
        break
    print("YES")
    break

# for i in range(0,len(height),1):
#     print(height[i], end=" ")



