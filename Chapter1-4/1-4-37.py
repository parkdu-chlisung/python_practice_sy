# 문제 37 : count 사용하기
# 새 학기를 맞아 은비네 반은 반장 선거를 하기로 했습니다.
# 그런데 표를 하나씩 개표하는 과정이 너무 번거롭게 느껴진 당신은 학생들이 뽑은 후보들을 입력받으면 
# 뽑힌 학생의 이름과 받은 표 수를 출력하는 프로그램을 작성하기로 했습니다.

x = (tuple(x) for x in input().split())

a = int(x.count("원영"))
b = int(x.count("은비"))
c = int(x.count("채연"))


if a > b and a > c:
    print("원영이가 총 ",a,"표로 반장이 되었습니다.")
elif b > a and b > c:
    print("은비가 총 ",b,"표로 반장이 되었습니다.")
elif c > a and c > b:
    print("채연이가 총 ",c,"표로 반장이 되었습니다.")
