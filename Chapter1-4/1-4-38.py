# 문제 38 : 호준이의 아르바이트 ******

# score = tuple([int(x) for x in input().split()])

# first = 0
# for i in range(0,len(score),1):
#     if score[i] >= first:
#         first = score[i]
# a = score.count(first)
# print(a)
# print(first)

# second = 0
# for i in range(0,len(score),1):
#     if score[i] >= second and first > second:
#         second = score[i]
# b = score.count(second)
# print(b)
# print(second)
        
# third = 0
# for i in range(0,len(score),1):
#     if score[i] >= third and second > third:
#         third = score[i]
# c = score.count(third)
# print(c)
# print(third)

# print(a+b+c)


data = input().split()
data = [int(i) for i in data]

count = 0

if len(set(data)) <= 3:
    count = len(data)
else :
    # 0, 1, 2 ,3 3은 4위의 점수
    break_point = sorted(list(set(data)), reverse=True)[3]
    data_sorted = sorted(data, reverse=True) # 데이터 정렬
    # sorted를 set으로 바꾼뒤(중복제거) 다시 정렬한다.

    for i in data_sorted:
        if break_point == i:
            break # 4위가 되었을 때 for문을 탈출한다.
        else:
            count += 1

print(count)