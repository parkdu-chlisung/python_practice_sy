# 문제 46 : str 자료형의 응용


x = ''
total = 0

for i in range(1,101):
    x += str(i)

for i in x:
    total += int(i)

print(total)

# ** 문제이해가 안됨