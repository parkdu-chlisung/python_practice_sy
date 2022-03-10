# 문제 45 : time함수 사용하기
import time


# time.time() -> 초를 반환한다.
secs = time.time()
# 365일 * 24시간 * 60분 * 60초 + 1970(1970년도부터 흐른 초를 알려줌)
# secs = secs // (365*24*60*60) + 1970

tm = time.localtime(secs)
print("year:", tm.tm_year)