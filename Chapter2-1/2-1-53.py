# 문제 53 : 괄호 문자열

# stack 사용하면 될거같음

user = list(input())
open = []
close = []

for i in user:
    if i == '(' or i == '[' or i == '{':
        open.append(i)
    else:
        close.append(i)

close.reverse()
print(open)
print(close)

if len(open) != len(close):
    print("NO(len)")
else :
    for i in range(len(open)):
        if open[i] == '(' and close[i] == ')':
            continue
        elif open[i] == '[' and close[i] == ']':
             continue
        elif open[i] == '{' and close[i] == '}':
             continue
        else:
            print("NO")
            exit()
    print("YES")
    exit()

