# 문제 45 : time함수 사용하기
import time


secs = time.time()
tm = time.localtime(secs)

print("year:", tm.tm_year)