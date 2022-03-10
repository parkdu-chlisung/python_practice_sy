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

# l.reverse()
# print(''.join(l))
# 이것도 가능

l = list(reversed(l))

for i in l:
    print(i, end="")


# bin(13) -> 빌트인펑션에 있음