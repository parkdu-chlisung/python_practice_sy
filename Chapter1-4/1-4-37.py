# 문제 37 : count 사용하기
# 새 학기를 맞아 은비네 반은 반장 선거를 하기로 했습니다.
# 그런데 표를 하나씩 개표하는 과정이 너무 번거롭게 느껴진 당신은 학생들이 뽑은 후보들을 입력받으면 
# 뽑힌 학생의 이름과 받은 표 수를 출력하는 프로그램을 작성하기로 했습니다.

data = input().split()
data_set = set(data)
data_dict = {}
for key in data_set:
    data_dict[key] = data.count(key)

print(f'{max(data_dict, key=data_dict.get)}(이)가 총 {max(data_dict.values())}표로 반장이 되었습니다.')

# **
# MAX, MIN, SORT 뒤에 key값 주는 것 많이 쓰임.
# {max(data_dict, key=data_dict.get)} 이렇게..
