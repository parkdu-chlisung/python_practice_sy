# 문제 43 : 10진수를 2진수로

x = int(input())
l = []

while (True) :
    if (x//2 != 0):
        l.append(int(x%2))
        x = x//2
    elif (x//2 ==0):
        l.append(int(x%2))
        break

l = list(reversed(l))

for i in l:
    print(i, end="")