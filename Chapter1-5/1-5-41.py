# 문제 41 : 소수판별
x = int(input())
for i in range(2,x-1,1):
    if x % i == 0:
        print("NO")
        break
    print("YES")
    break