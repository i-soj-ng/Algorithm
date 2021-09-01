n = int(input())

while True:
    n_list = list(map(int, str(n)))
    result = True

    for i in range(len(n_list)//2):
        if n_list[i] != n_list[len(n_list)-1-i]:
            result = False

    if result:
        print(n)
        break
    else:
        n += 1
