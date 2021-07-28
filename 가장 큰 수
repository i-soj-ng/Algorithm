# 문제: https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse = True)
    
    # numbers가 [0, 0, 0]일 때, 그냥 join해버리면 answer = "000"이 됨. 이를 해결하기 위해 조건문 사용
    if numbers[0] == '0':
        answer = "0"
    
    else:
        answer = "".join(numbers)
    
    return answer
