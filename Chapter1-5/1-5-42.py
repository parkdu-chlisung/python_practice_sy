# 문제 42 : 2020년

# 2020년 1월 1일 (수)
# 2목 3금 4토 5일 6월 7화 8수
# 2   3   4   5   6   0   1 (7%)

# 1월 - 31일
# 2월 - 28일 59
# 3월 - 31일 90
# 4월 - 30일120
# 5월 - 31일151
# 6월 - 30일181
# 7월 - 31일212
# 8월 - 31일243
# 9월 - 30일273
# 10월 - 31일304
# 11월 - 30일334
# 12월 - 31일365

month = int(input())
day=int(input())

def dayTotal(month,day):
    if month==1:
        dayTotal=day
    elif month==2:
        dayTotal=31+day
    elif month==3:
        dayTotal=59+day
    elif month==4:
        dayTotal=91+day
    elif month==5:
        dayTotal= 121+day
    elif month==6:
        dayTotal= 152+day
    elif month==7:
        dayTotal=182+day
    elif month==8:
        dayTotal=213+day
    elif month==9:
        dayTotal=244+day
    elif month==10:
        dayTotal=274+day
    elif month==11:
        dayTotal=305+day
    elif month==12:
        dayTotal=335+day
    
    result = dayTotal % 7
    if result == 0:
        return "TUE"
    elif result == 1:
        return "WED"
    elif result == 2:
        return "THU"
    elif result == 3:
        return "FRI"
    elif result == 4:
        return "SAT"
    elif result == 5:
        return "SUN"
    elif result == 6:
        return "MON"

    
print(dayTotal(month,day))