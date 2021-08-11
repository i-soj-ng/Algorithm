# 문제: https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    answer = -1
    n = 0
    total = 0

    while count != 0:
        n += 1
        total += price * n
        count -= 1
    
    answer = money - total
    
    if answer >= 0: # 돈이 부족하지 않은 경우 0을 반환함
        return 0
    else:
        return abs(answer)
      
