# 문제 38 : 호준이의 아르바이트
# 호준이는 아르바이트로 영어 학원에서 단어 시험지를 채점하는 일을 하고 있다.
# 호준이가 일하는 학원은 매번 1위부터 8위까지 학생에게 상으로 사탕을 준다.
# 그런데 오늘은 마침 사탕이 다 떨어져서 호준이가 채점을 하고 점수를 보내면, 당신이 아이들의 숫자만큼 사탕을 사러 가기로 했다.

# 학생들의 점수를 공백으로 구분하여 입력받는다. 1위 ~ 3위 학생은 여러명일 수 있고 1 ~ 3위 학생 중 중복되는 학생까지 포함하여 사탕을 사기로 한다.

score = tuple([int(x) for x in input().split()])

first = 0
for i in range(0,len(score),1):
    if score[i] >= first:
        first = score[i]
a = score.count(first)
print(a)
print(first)

second = 0
for i in range(0,len(score),1):
    if score[i] >= second and first > second:
        second = score[i]
b = score.count(second)
print(b)
print(second)
        
third = 0
for i in range(0,len(score),1):
    if score[i] >= third and second > third:
        third = score[i]
c = score.count(third)
print(c)
print(third)

print(a+b+c)
