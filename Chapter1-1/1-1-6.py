# 문제 6 : False
# 다음은 파이썬 문법 중에서 False로 취급하는 것들 입니다.
# False로 취급하지 않는 것이 하나 있습니다. True를 찾아주세요.

# 1) None -> 거짓
# 2) 1 -> 참
# 3) ""  -> 거짓
# 4) 0 -> 거짓
# 5) bool(0) -> 거짓

print(bool(None))
print(bool(1))
print(bool(""))
print(bool(0))
print(bool(0))

# 2번 ) 1-> 참
# 0을 제외한 모든 숫자는 참이다.**
# 자료형 안에 값이 아무것도 없으면 false이다. "", [] 
# 주의 ) " " 스페이스가 들어가 있으면, 스페이스가 들어가 있기에 True

print(bool(" ")) 
print(bool(""))
print(bool(["",""]))
print(bool([]))
print(bool(None))

# Ture -> 스페이스 한칸 띔 True
# False -> 아무것도 없으니까 False
# True -> 리스트 안에 아무것도 없는 문자열 두개 (컴마가 있기에 True로 잡힘)
# False -> 리스트 자체에 아무 값도 없음
# False -> None 