# 문제URL: https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = 0
    variety = len(set(nums))
    half = len(nums) // 2
    
    if variety > half:
        answer = half
    else:
        answer = variety
        
    return answer
