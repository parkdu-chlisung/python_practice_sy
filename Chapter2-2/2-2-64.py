# 문제 64 : 이상한 엘레베이터

weight = int(input())

def test(weight) :
    three = 0
    seven = weight / 7
    result1 = three + seven
    
    three = weight / 3
    seven = 0
    result2 = three + seven
        
    seven = weight // 7
    three =  ( weight - 7 * seven ) // 3
    result3 = three + seven

    if ((result1 < result2) & (result1 < result3) & (result1 % 1 == 0)) :
        print(result1)
    elif ((result2 < result1) & (result2 < result3) & (result2 % 1 == 0)) :
        print(result2)
    else :
        print(result3)

if ((weight % 7 == 0) | (weight % 3 == 0 ) | (weight % 21 == 0)) :
    test(weight)
else :
    print("-1")