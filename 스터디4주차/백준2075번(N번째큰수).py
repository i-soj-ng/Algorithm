# 문제: https://www.acmicpc.net/problem/2075
import heapq
n = int(input())
heap = [] # 최소 힙

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if i == 0:
            heapq.heappush(heap, temp[j])
        else:
            if temp[j] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, temp[j])
            else:
                continue

print(heapq.heappop(heap))
