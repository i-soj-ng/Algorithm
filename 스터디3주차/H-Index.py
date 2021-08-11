# 문제: https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse=True)
    for i, n in enumerate(citations):
        if n <= i:
            return i
    return len(citations)
  
