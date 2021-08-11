# 문제: https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    
    for (i, j, k) in commands:
        sliced_arr = array[i-1:j]
        sliced_arr.sort()
        answer.append(sliced_arr[k-1])
        
    return answer
  
