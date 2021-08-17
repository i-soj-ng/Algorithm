# 문제: https://www.acmicpc.net/problem/1976
def find(cities, x):
    if cities[x] != x:
        cities[x] = find(cities, cities[x])
    return cities[x]

def union(cities, a, b):
    a = find(cities, a)
    b = find(cities, b)
    if a < b:
        cities[b] = a
    else:
        cities[a] = b


n = int(input())
m = int(input())
cities = [0] * (n + 1)

for i in range(1, n + 1):
    cities[i] = i

for i in range(n):
    graph = list(map(int, input().split()))
    for j in range(n):
        if graph[j] == 1:
            union(cities, i+1, j+1)

plan = list(map(int, input().split()))

result = 'YES'
for i in range(m-1):
    if find(cities, plan[i]) != find(cities, plan[i+1]):
        result = 'NO'

print(result)