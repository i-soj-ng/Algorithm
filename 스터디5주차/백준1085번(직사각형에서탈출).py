# 문제: https://www.acmicpc.net/problem/1085

x, y, w, h = map(int, input().split())
length = [x, y, w-x, h-y]
print(min(length))
