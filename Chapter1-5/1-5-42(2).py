# datetime 모듈 사용

import datetime

m=int(input())
d = int(input())

def findDay(a,b):
    day = ["MON", "TUE", "WED", "THU", "FRI","SAT","SUN"]
    return day[datetime.date(2021,a,b).weekday()]

print(findDay(m,d))