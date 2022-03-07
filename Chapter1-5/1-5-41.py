# 문제 41 : 소수판별 *****
x = int(input())
for i in range(3,x):
    if x <= 1:
        print("NO")
        break
    elif x ==2:
        print("NO")
        break
    elif x % i == 0:
        print("NO")
        break
    else:
        print("YES")
        break