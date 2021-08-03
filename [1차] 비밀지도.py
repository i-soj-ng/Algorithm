# 문제: https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        map1 = ''
        b1 = list(format(arr1[i], 'b'))
        b2 = list(format(arr2[i], 'b'))
        
        # 변환된 이진수의 길이가 n보다 작으면 아래의 for문에서 인덱스에러가 발생함.
        # 이를 방지하기 위해 n보다 작은 만큼 이진수의 앞에 0을 추가하여 이진수의 길이가 n이 되도록 함.
        temp = n - len(b1)
        for t in range(temp):
            b1.insert(0, '0')
            
        temp = n - len(b2)
        for t in range(temp):
            b2.insert(0, '0')
            
        for j in range(n):
            if b1[j] == '0' and b2[j] == '0':
                map1 += ' '
            else:
                map1 += '#'
                
        answer.append(map1)
        
    return answer
