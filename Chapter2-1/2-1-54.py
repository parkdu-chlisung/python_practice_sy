# 문제 54 : 연속되는 수

num = list(map(int, input().split()))
num.sort()

for i in range(len(num)-1):
    if num[i + 1] == num[i] + 1:
        continue
    else:
        print("NO")
        exit()
print("YES")
exit()