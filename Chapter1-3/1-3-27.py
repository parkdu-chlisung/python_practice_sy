# 문제 27 : 딕셔너리 만들기
# 첫 줄에는 학생의 이름이 공백으로 구분되어 입력되고,
# 두번째 줄에는 그 학생의 수학 점수가 공백으로 구분되어 주어집니다.
# 두 개를 합쳐 학생의 이름이 key이고 value가 수학 점수인 딕셔너리를 출력해주세요.

student1, student2 = map(str, input().split())
score1, score2 = map(int, input().split())

dic = {student1 : score1 , student2 : score2}
print(dic)