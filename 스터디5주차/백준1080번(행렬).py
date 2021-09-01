n, m = map(int, input().split())
count = 0

A = []
for i in range(n):
    A.append(list(map(int, input())))

B = []
for i in range(n):
    B.append(list(map(int, input())))

def change(x, y, arr):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 - A[i][j]

for i in range(0, n-2):
    for j in range(0, m-2):
        if A[i][j] != B[i][j]:
            change(i, j, A)
            count += 1

result = False
for i in range(0, n):
    for j in range(0, m):
        if A[i][j] != B[i][j]:
            result = True

if (result):
    print(-1)
else:
    print(count)